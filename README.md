# :partly_sunny: WLAN-Wetterstation
<br/><br/>
[![License](https://img.shields.io/github/license/SBorg2014/WLAN-Wetterstation.svg)](https://github.com/SBorg2014/WLAN-Wetterstation/blob/master/LICENSE). 


Implementiert einen kleinen Wunderground-Server als flask python-webapp und schafft eine Verbindung zu einer WLAN-Wetterstation. 
Es stellt die Wetterdaten in [openSenseMap](https://opensensemap.org) zur Verfügung. (__Projekt läuft nur unter Linux__)<br>
Portiert [SBorg2014/WLAN-Wetterstation](https://github.com/SBorg2014/WLAN-Wetterstation) from bash to a lightweight python script.

## Verwendung
```bash
git clone https://github.com/Whadup/WLAN-Wetterstation
cd WLAN-Wetterstation
#Configure sensebox id in app.py
#Configure login and passwords
printf "{email}\n{password}\n{sensebox-auth-token}\n" > osm-credentials.txt
flask run
```
 
 Die Wetterstation muss dazu in der Lage sein ihre Daten im "Wunderground"-Format zu senden.<br><br>
 Bisher getestete Stationen:
- DNT Weatherscreen PRO
- ELV WS980WiFi
- Eurochron EFWS 2900 (baugleich zu Sainlogic 10in1 Wifi, Ambient Weather WS-2902, Chilitec CTW-902 Wifi)
- Froggit
  * HP1000SE Pro
  * WH3000 SE
  * WH4000 SE
- Renkforce WH2600
- Sainlogic 7in1 WiFi WS3500
- Ventus W830
<br><br>

Zusatzsensoren (mittels Station oder Gateway DP1500/GW1000):
- bis zu 8 Stück DP50/WH31 Temperatur-/Luftfeuchtigkeit-Sensoren
- ein DP60/WH57 Blitzsensor
- bis zu 4 Stück DP70/WH55 Wasserleckage-Sensoren
- bis zu 8 Stück DP100/WH51 Bodenfeuchte-Sensoren
- bis zu 4 Stück DP200/WH43 PM2.5 Feinstaub-Sensoren
<br><br>


Experimentell (über eigenen DNS-Server):
- Stationen ohne Möglichkeit der Konfiguration mittels App *WS View* wie bspw. *Sainlogic Profi Wlan Wetterstation FT0300*
- Installation siehe [WiKi](https://github.com/SBorg2014/WLAN-Wetterstation/wiki/Installation---eigener-DNS-Server)
<br><br>


<br><br>
## :scroll: License ## 
 MIT License

Copyright (c)2021 by Whadup

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
