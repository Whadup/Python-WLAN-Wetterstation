import sys
import requests
from requests_jwt import JWTAuth

import logging
import json

SENSOR_NAMES = ["Temperatur", "Luftfeuchte", "Luftdruck relativ", "Luftdruck absolut", "Taupunkt", "gefühlte Temperatur", "Sonnenstrahlung", "Windgeschwindigkeit", "Windrichtung", "UV-Index", "Regen-Rate"]
  #Messwertezuordnung (Reihenfolge muss zur Sensor-ID identisch sein!)
SENSOR_FIELDS = ["tempf", "humidity", "baromrelin", "baromabsin", "dewptf", "windchillf", "solarradiation", "windspeedmph", "winddir", "uv", "rainratein"]
  #Sensorendefinitionen
SENSOR_ICONS = ["osem-thermometer", "osem-humidity", "osem-barometer", "osem-barometer", "osem-thermometer", "osem-thermometer", "osem-brightness", "osem-particulate-matter", "osem-particulate-matter", "osem-brightness", "osem-umbrella"]
SENSOR_UNITS = ['°C', '%H', 'hPa', 'hPa', '°C', '°C', 'W/m²', 'km/h', '°', 'Index', 'mm/h']
SENSORS = list(zip(SENSOR_NAMES, SENSOR_FIELDS, SENSOR_ICONS, SENSOR_UNITS))

def login(config):
    try:
        url = "https://api.opensensemap.org/users/sign-in"
        credentials = open("osm-credentials.txt", "r").read().split("\n")
        response = requests.post(url, json=dict(email=credentials[0], password=credentials[1])).json()
        config["JWT"] = response["token"]
        config["REFRESH"] = response["refreshToken"]
        return True
    except:
        return False


def relogin(config):
    pass

def initialize_osm(config):
    if not login(config):
        raise RuntimeError("Login failed")
    if not get_sensors(config):
        register_sensors(config)

def get_sensors(config):
    url = f"https://api.opensensemap.org/boxes/{config['SENSEBOX_ID']}"
    
    try:
        sensor = requests.get(url).json()
        # if len(sensor.get("sensors", [])) == len(SENSORS):
        config["SENSOR_IDS"] = {}
        delete_sensors = []
        for s in sensor["sensors"]:
            if s["title"] in SENSOR_NAMES:
                i = SENSOR_NAMES.index(s["title"])
                config["SENSOR_IDS"][SENSOR_FIELDS[i]] = s["_id"]
            else:
                delete_sensors.append(s["_id"])
                print(f"Sensor {s['title']} is configured at osm, but not in this server.")
        if len(delete_sensors) > 0:
            import os
            if os.environ.get("DELETE_OLD_SM_SENSORS", None) is not None:
                print("Deleting sensors", delete_sensors)
                
                sensors = []
                for s in delete_sensors:
                    sensors.append(dict(deleted="true",_id=s))
                request = dict(sensors=sensors)
                url = f"https://api.opensensemap.org/boxes/{config['SENSEBOX_ID']}"
                resp = requests.put(url, json=request, headers={"Authorization": f"Bearer {config['JWT']}"})
            else:
                print("I could delete sensors", delete_sensors)
                print("To go ahead, set the DELETE_OLD_SM_SENSORS environment variable")
        if len(config["SENSOR_IDS"]) == len(SENSORS):
            print("Matched all sensors")
            print(config["SENSOR_IDS"])
            return True
        else:
            print("Not all sensors found. Going to recreate all of them. Might result in chaos...")
            return False
            # print("we are gonna delete the old sensors. this shouldn't remain in the code...")
            # sensors = []
            # for s in sensors:
            #     sensors.append(dict(deleted="true",_id=s["605741e529171e001b21cd17"]))
            # request = dict(sensors=sensors)
            # url = f"https://api.opensensemap.org/boxes/{config['SENSEBOX_ID']}"
            # resp = requests.put(url, json=request, headers={"Authorization": f"Bearer {config['JWT']}"})
            # print(resp)
            # print("Wrong number of Sensors")
    except Exception as e:
        print(e)
        return False

def register_sensors(config):
    # return
    sensors = []
    for sensor in SENSORS:
        name, field, icon, unit = sensor
        sensors.append(dict(
            new="true",
            edited="true",
            title=name,
            unit=unit,
            sensorType="Wetterstation",
            icon=icon
        ))
    request = dict(sensors=sensors)
    url = f"https://api.opensensemap.org/boxes/{config['SENSEBOX_ID']}"
    
    resp = requests.put(url, json=request, headers={"Authorization": f"Bearer {config['JWT']}"})
    print(resp.text)

def hitzeindex(temp, feuchte):
    number = -8.784695
    number += 1.61139411 * temp
    number += 2.338549 * feuchte
    number -= 0.14611605 * temp * feuchte
    number -= 0.012308094 * (temp ** 2)
    number -= 0.016424828 * (feuchte ** 2)
    number += 0.002211732 * (temp ** 2) * feuchte
    number += 0.00072546 * temp * (feuchte ** 2)
    number -= 0.000003582 * (temp** 2) * (feuchte ** 2)
    return number