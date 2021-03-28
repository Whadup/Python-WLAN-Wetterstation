#      if [[ ${MESSWERTERAWIN[$i]} == tempinf=* ]] || [[ ${MESSWERTERAWIN[$i]} == indoortempf=* ]]
#         then MESSWERTE[0]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertFtoC 0; fi
#      if [[ ${MESSWERTERAWIN[$i]} == tempf=* ]]
#         then MESSWERTE[1]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertFtoC 1; fi
#      if [[ ${MESSWERTERAWIN[$i]} == dewptf=* ]]
#         then MESSWERTE[2]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertFtoC 2; fi
#      if [[ ${MESSWERTERAWIN[$i]} == windchillf=* ]]
#         then MESSWERTE[3]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertFtoC 3; fi
#      if [[ ${MESSWERTERAWIN[$i]} == humidityin=* ]] || [[ ${MESSWERTERAWIN[$i]} == indoorhumidity=* ]]
#         then MESSWERTE[4]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == humidity=* ]]
#         then MESSWERTE[5]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == windspeedmph=* ]]
#         then MESSWERTE[6]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertMPHtoKMH 6; fi
#      if [[ ${MESSWERTERAWIN[$i]} == windgustmph=* ]]
#         then MESSWERTE[7]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertMPHtoKMH 7; fi
#      if [[ ${MESSWERTERAWIN[$i]} == winddir=* ]]
#         then MESSWERTE[8]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); winddir 8; fi
#      if [[ ${MESSWERTERAWIN[$i]} == baromabsin=* ]] || [[ ${MESSWERTERAWIN[$i]} == absbaromin=* ]]
#         then MESSWERTE[9]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertLuftdruck 9; fi
#      if [[ ${MESSWERTERAWIN[$i]} == baromrelin=* ]] || [[ ${MESSWERTERAWIN[$i]} == baromin=* ]]
#         then MESSWERTE[10]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertLuftdruck 10; fi
#      if [[ ${MESSWERTERAWIN[$i]} == rainratein=* ]] || [[ ${MESSWERTERAWIN[$i]} == rainin=* ]]
#         then MESSWERTE[11]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 11; fi
#      if [[ ${MESSWERTERAWIN[$i]} == dailyrainin=* ]]
#         then MESSWERTE[12]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 12; fi
#      if [[ ${MESSWERTERAWIN[$i]} == weeklyrainin=* ]]
#         then MESSWERTE[13]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 13; fi
#      if [[ ${MESSWERTERAWIN[$i]} == monthlyrainin=* ]]
#         then MESSWERTE[14]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 14; fi
#      if [[ ${MESSWERTERAWIN[$i]} == yearlyrainin=* ]]
#         then MESSWERTE[15]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 15; fi
#      if [[ ${MESSWERTERAWIN[$i]} == solarradiation=* ]]
#         then MESSWERTE[16]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); sonnenpuls 16; fi
#      if [[ ${MESSWERTERAWIN[$i]} == uv=* ]] || [[ ${MESSWERTERAWIN[$i]} == UV=* ]]
#         then MESSWERTE[17]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); uv_belastung 17; fi
#      if [[ ${MESSWERTERAWIN[$i]} == dateutc=* ]]
#         then MESSWERTE[18]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertTime 18; fi
#      if [[ ${MESSWERTERAWIN[$i]} == stationtype=* ]] || [[ ${MESSWERTERAWIN[$i]} == softwaretype=* ]]
#         then MESSWERTE[19]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == wh65batt=* ]]
#         then MESSWERTE[20]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == maxdailygust=* ]]
#         then MESSWERTE[21]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertMPHtoKMH 21; fi
#      if [[ ${MESSWERTERAWIN[$i]} == eventrainin=* ]]
#         then MESSWERTE[22]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 22; fi
#      if [[ ${MESSWERTERAWIN[$i]} == hourlyrainin=* ]]
#         then MESSWERTE[23]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 23; fi
#      if [[ ${MESSWERTERAWIN[$i]} == totalrainin=* ]]
#         then MESSWERTE[24]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convertInchtoMM 24; fi
#      if [[ ${MESSWERTERAWIN[$i]} == model=* ]]
#         then MESSWERTE[25]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi'

def convertFtoC(x):
    return (float(x) - 32.0) * 5.0 / 9.0

def convertMPHtoKMH(x):
    return float(x) * 16094.0 / 10000.0

_WIND_DIRS = [
    "N", "NNO", "NO",
    "ONO", "O", "OSO",
    "SO", "SSO", "S", "SSW", "SW",
    "WSW", "W", "WNW",
    "NW", "NNW", "N"
]

def winddir(x):
    #WINDRICHTUNG=${WINDDIRS[$(round ${MESSWERTE[$1]}/22.5 0)]}
    return _WIND_DIRS[int(float(x) / 22.5)]

def convertLuftdruck(x):
    return float(x) * 33864 / 1000.0

def convertInchtoMM(x):
    return float(x) * 254 / 10.0
    #TODO THIS DOES A LOT MORE IN THE ORIGINAL

def sonnenpuls(x):
    return x

def uv_belastung(x):
    return x

def convertTime(x):
    return x







_fields = [
    ("tempinf", "indoortempf"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == indoortempf=*
    "tempf",#=*
    "dewptf",#=*
    "windchillf",#=*
    ("humidityin", "indoorhumidity"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == indoorhumidity=*
    "humidity",#=*
    "windspeedmph",#=*
    "windgustmph",#=*
    "winddir",#=*
    ("baromabsin", "absbaromin"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == absbaromin=*
    ("baromrelin", "baromin"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == baromin=*
    ("rainratein", "rainin"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == rainin=*
    "dailyrainin",#=*
    "weeklyrainin",#=*
    "monthlyrainin",#=*
    "yearlyrainin",#=*
    "solarradiation",#=*
    ("uv", "UV"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == UV=*
    "dateutc",#=*
    ("stationtype", "softwaretype"), #=* ]] || [[ ${MESSWERTERAWIN[$i]} == softwaretype=*
    "wh65batt",#=*
    "maxdailygust",#=*
    "eventrainin",#=*
    "hourlyrainin",#=*
    "totalrainin",#=*
    "model",#=*
]

_processing = [
    convertFtoC,
    convertFtoC,
    convertFtoC,
    convertFtoC,
    float,
    float,
    convertMPHtoKMH,
    convertMPHtoKMH,
    winddir,
    convertLuftdruck,
    convertLuftdruck,
    convertInchtoMM,
    convertInchtoMM,
    convertInchtoMM,
    convertInchtoMM,
    convertInchtoMM,
    sonnenpuls,
    uv_belastung,
    convertTime,
    None,
    None,
    convertMPHtoKMH,
    convertInchtoMM,
    convertInchtoMM,
    convertInchtoMM,
    None
]

fields = {}
processing = {}
for v, p in zip(_fields, _processing):
    if isinstance(v, tuple):
        for u in v:
            fields[u] = v[0]
            processing[v[0]] = p
    else:
        fields[v] = v
        processing[v] = p