import requests
from datetime import datetime
 
MY_LAT = 10.9666666667
MY_LONG = 106.6666666667

parameters ={
    "lat": MY_LAT,
    "lng": MY_LONG,
}

reponse = requests.get("https://api.sunrisesunset.io/json", params=parameters)
reponse.raise_for_status()
data = reponse.json()
sunrise = data["results"]["sunrise"].split(":")[0]
sunset = data["results"]["sunset"].split(":")[0]
print(f"Surise: {sunrise} AM\nSunset: {sunset} PM")


time_now = datetime.now()
print(f"Now: {time_now.hour}h")