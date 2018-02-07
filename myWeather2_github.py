# myWeather.py  for inkyphat and RPiZW

print('Starting')
try:
    import requests
    print('requests module imported')
except:
    print('Sorry, need to install requests module')
    exit()
wx_url = 'api.openweathermap.org/data/2.5/weather?'
wx_city = 'q=Quispamsis,CA&units=metric'
wx_cityID = 'id=6115383&units=metric'

api_key = '&APPID='+'ENTER YOUR API KEY HERE'

try:
    resp = requests.get('http://'+wx_url+wx_cityID+api_key)
    print('got data')
except:
    print('Cannot connect to service...')
    exit()
if resp.status_code != 200:
    raise ApiError('GET /weather/ {}'.format(resp.status_code))

try:
    city=resp.json()["name"]
    temperature=resp.json()["main"]["temp"]    # in celcius
    pressure=resp.json()["main"]["pressure"]   # in hPa
    humidity=resp.json()["main"]["humidity"]   # in %
    windSpeed = resp.json()["wind"]["speed"]   # in m/s
    windDeg = resp.json()["wind"]["deg"]
    print('got json info')
    
except:
    print('Cannot read data in api call...')
    exit()
print('Weather in', city+':')
print('\tTemperature:\t',str(temperature)+'°C')
print('\tPressure:\t',pressure,'hPa')
print('\tWind:\t\t',windSpeed,'m/s from',str(windDeg)+'°')
print('\tWind:\t\t',
      round(windSpeed*0.277778,1),'km/h from',str(windDeg)+'°')
