#!/bin/bash
#!/usr/bin/env bash

_term() { 
  echo "Caught SIGTERM signal!" 
  kill -TERM "$child" 2>/dev/null
}
sleep 10
trap _term SIGTERM
cd /home/pi/WLAN-Wetterstation
while true
do
flask run -h 0.0.0.0 -p 5555&
child=$!
wait "$child"
done
