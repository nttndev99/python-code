import requests

# https://api.openweathermap.org/data/2.5/forecast?lat=10.735299&lon=106.671878&cnt=3&appid=0e4be2694917730c00d2b5a72b4199f2
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "0e4be2694917730c00d2b5a72b4199f2"

weather_params = {
    "lat": 10.735299,    
    "lon": 106.671878,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Probability of rain !!!")