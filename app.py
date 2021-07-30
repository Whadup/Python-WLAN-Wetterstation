import json
import base64
import os
from datetime import datetime
from flask import Flask, Response
from flask import request
from flask import current_app
import requests
from fields import FIELDS, PROCESSING
from osm import initialize_osm, SENSORS



app = Flask(__name__)
app.osm_data = []
app.config.update(dict(
    SECRET_KEY=base64.b64encode(os.urandom(64)).decode('utf-8'),
    # SERVER_NAME='0.0.0.0:5555',
    SENSEBOX_ID="605f498077a88b001bba3dc0",
    SENSEBOX_AUTHORIZATION=open("osm-credentials.txt", "r").read().split("\n")[2],
))
with app.app_context():
    initialize_osm()


@app.route("/weatherstation/updateweatherstation.php")
def update():
    #print(request.args)
    local_time = datetime.utcnow()

    # get the FIELDS
    sensor_values = {}
    for argument in request.args:
        if argument in FIELDS:
            sensor_name = FIELDS[argument]
            if PROCESSING.get(sensor_name, None) is not None:
                sensor_value = PROCESSING.get(sensor_name)(request.args.get(argument))
            else:
                sensor_value = request.args.get(argument)
            sensor_values[sensor_name] = sensor_value


    # push to opensensormap
    timestamp = local_time.isoformat() + "Z"

    for sensor_name in sensor_values:
        if sensor_name in current_app.config["SENSOR_IDS"]:
            _id = current_app.config["SENSOR_IDS"][sensor_name]
            val = sensor_values[sensor_name]
            current_app.osm_data.append(dict(sensor=_id, value=str(val), createdAt=timestamp))
    if len(current_app.osm_data) > len(SENSORS) * 4:
        url = f"https://api.opensensemap.org/boxes/{current_app.config['SENSEBOX_ID']}/data"
        try:
            #print(json.dumps(current_app.osm_data))
            response = requests.post(url, json=current_app.osm_data, headers={"Authorization": current_app.config["SENSEBOX_AUTHORIZATION"]})
            response.raise_for_status()
            current_app.osm_data.clear()
        except requests.ConnectionError as e:
            print(e)
        except requests.Timeout as e:
            print(e)
        except request.HTTPError as e:
            print(e)
    return Response(status=200)



if __name__ == "__main__":
    app.run()
