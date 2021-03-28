from datetime import datetime
import base64, os
from flask import Flask, Response
from flask import request
from flask import current_app
from fields import fields, processing
from osm import *
import requests.cookies
app = Flask(__name__)
app.osm_data = []
app.config.update(dict(
    SECRET_KEY=base64.b64encode(os.urandom(64)).decode('utf-8'),
    SERVER_NAME='127.0.0.1:5555',
    SENSEBOX_ID="605f498077a88b001bba3dc0",
    SENSEBOX_AUTHORIZATION=open("osm-credentials.txt", "r").read().split("\n")[2],
))
initialize_osm(app.config)


@app.route("/weatherstation/updateweatherstation.php")
def update():
    print(request.args)
    local_time = datetime.utcnow()
    
    # get the fields
    sensor_values = {}
    for argument in request.args:
        if argument in fields:
            sensor_name = fields[argument]
            if processing.get(sensor_name, None) is not None:
                sensor_value = processing.get(sensor_name)(request.args.get(argument))
            else:
                sensor_value = request.args.get(argument)
            sensor_values[sensor_name] = sensor_value
    print(sensor_values)
    timestamp = local_time.isoformat() + "Z"
    
    for sensor_name in sensor_values:
        if sensor_name in current_app.config["SENSOR_IDS"]:
            _id = current_app.config["SENSOR_IDS"][sensor_name]
            val = sensor_values[sensor_name]
            current_app.osm_data.append(dict(sensor=_id, value=val, createdAt=timestamp))
    if True or len(current_app.osm_data) > len(SENSORS) * 4:
        url = f"https://api.opensensemap.org/boxes/{current_app.config['SENSEBOX_ID']}/data"
        try:
            print(json.dumps(current_app.osm_data))
            response = requests.post(url, json=current_app.osm_data, headers={"Authorization": current_app.config["SENSEBOX_AUTHORIZATION"]})
            response.raise_for_status()
            current_app.osm_data.clear()
        except Exception as e:
            print(e)
    # push to opensensormap
    return Response(status=200)



if __name__ == "__main__":
    # init_db()
    app.run()
