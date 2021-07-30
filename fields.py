#      if [[ ${MESSWERTERAWIN[$i]} == tempinf=* ]] || [[ ${MESSWERTERAWIN[$i]} == indoortempf=* ]]
#         then MESSWERTE[0]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_F_to_C 0; fi
#      if [[ ${MESSWERTERAWIN[$i]} == tempf=* ]]
#         then MESSWERTE[1]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_F_to_C 1; fi
#      if [[ ${MESSWERTERAWIN[$i]} == dewptf=* ]]
#         then MESSWERTE[2]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_F_to_C 2; fi
#      if [[ ${MESSWERTERAWIN[$i]} == windchillf=* ]]
#         then MESSWERTE[3]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_F_to_C 3; fi
#      if [[ ${MESSWERTERAWIN[$i]} == humidityin=* ]] || [[ ${MESSWERTERAWIN[$i]} == indoorhumidity=* ]]
#         then MESSWERTE[4]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == humidity=* ]]
#         then MESSWERTE[5]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == windspeedmph=* ]]
#         then MESSWERTE[6]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_MPH_to_KMH 6; fi
#      if [[ ${MESSWERTERAWIN[$i]} == windgustmph=* ]]
#         then MESSWERTE[7]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_MPH_to_KMH 7; fi
#      if [[ ${MESSWERTERAWIN[$i]} == winddir=* ]]
#         then MESSWERTE[8]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); winddir 8; fi
#      if [[ ${MESSWERTERAWIN[$i]} == baromabsin=* ]] || [[ ${MESSWERTERAWIN[$i]} == absbaromin=* ]]
#         then MESSWERTE[9]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_luftdruck 9; fi
#      if [[ ${MESSWERTERAWIN[$i]} == baromrelin=* ]] || [[ ${MESSWERTERAWIN[$i]} == baromin=* ]]
#         then MESSWERTE[10]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_luftdruck 10; fi
#      if [[ ${MESSWERTERAWIN[$i]} == rainratein=* ]] || [[ ${MESSWERTERAWIN[$i]} == rainin=* ]]
#         then MESSWERTE[11]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 11; fi
#      if [[ ${MESSWERTERAWIN[$i]} == dailyrainin=* ]]
#         then MESSWERTE[12]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 12; fi
#      if [[ ${MESSWERTERAWIN[$i]} == weeklyrainin=* ]]
#         then MESSWERTE[13]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 13; fi
#      if [[ ${MESSWERTERAWIN[$i]} == monthlyrainin=* ]]
#         then MESSWERTE[14]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 14; fi
#      if [[ ${MESSWERTERAWIN[$i]} == yearlyrainin=* ]]
#         then MESSWERTE[15]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 15; fi
#      if [[ ${MESSWERTERAWIN[$i]} == solarradiation=* ]]
#         then MESSWERTE[16]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); sonnenpuls 16; fi
#      if [[ ${MESSWERTERAWIN[$i]} == uv=* ]] || [[ ${MESSWERTERAWIN[$i]} == UV=* ]]
#         then MESSWERTE[17]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); uv_belastung 17; fi
#      if [[ ${MESSWERTERAWIN[$i]} == dateutc=* ]]
#         then MESSWERTE[18]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_time 18; fi
#      if [[ ${MESSWERTERAWIN[$i]} == stationtype=* ]] || [[ ${MESSWERTERAWIN[$i]} == softwaretype=* ]]
#         then MESSWERTE[19]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == wh65batt=* ]]
#         then MESSWERTE[20]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi
#      if [[ ${MESSWERTERAWIN[$i]} == maxdailygust=* ]]
#         then MESSWERTE[21]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_MPH_to_KMH 21; fi
#      if [[ ${MESSWERTERAWIN[$i]} == eventrainin=* ]]
#         then MESSWERTE[22]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 22; fi
#      if [[ ${MESSWERTERAWIN[$i]} == hourlyrainin=* ]]
#         then MESSWERTE[23]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 23; fi
#      if [[ ${MESSWERTERAWIN[$i]} == totalrainin=* ]]
#         then MESSWERTE[24]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); convert_Inch_to_MM 24; fi
#      if [[ ${MESSWERTERAWIN[$i]} == model=* ]]
#         then MESSWERTE[25]=$(echo ${MESSWERTERAWIN[$i]}|cut -d"=" -f2); fi'

def convert_F_to_C(x):
    return (float(x) - 32.0) * 5.0 / 9.0

def convert_MPH_to_KMH(x):
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
    return float(x)
    return _WIND_DIRS[int(float(x) / 22.5)]

def convert_luftdruck(x):
    return float(x) * 33864 / 1000.0

def convert_Inch_to_MM(x):
    return float(x) * 254 / 10.0
    #TODO THIS DOES A LOT MORE IN THE ORIGINAL

def sonnenpuls(x):
    return x

def uv_belastung(x):
    return x

def convert_time(x):
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
    convert_F_to_C,
    convert_F_to_C,
    convert_F_to_C,
    convert_F_to_C,
    float,
    float,
    convert_MPH_to_KMH,
    convert_MPH_to_KMH,
    winddir,
    convert_luftdruck,
    convert_luftdruck,
    convert_Inch_to_MM,
    convert_Inch_to_MM,
    convert_Inch_to_MM,
    convert_Inch_to_MM,
    convert_Inch_to_MM,
    sonnenpuls,
    uv_belastung,
    convert_time,
    None,
    None,
    convert_MPH_to_KMH,
    convert_Inch_to_MM,
    convert_Inch_to_MM,
    convert_Inch_to_MM,
    None
]

FIELDS = {}
PROCESSING = {}
for v, p in zip(_fields, _processing):
    if isinstance(v, tuple):
        for u in v:
            FIELDS[u] = v[0]
            PROCESSING[v[0]] = p
    else:
        FIELDS[v] = v
        PROCESSING[v] = p
