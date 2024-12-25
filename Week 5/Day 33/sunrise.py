import requests
import datetime

LATITUDE = 49.319538
LONGITUDE = 7.334330

date = datetime.datetime.now()
date_string = date.strftime("%m/%d/%Y, %H:%M:%S")
print(date_string)

parameters = {
    "lat" : LATITUDE,
    "lng" : LONGITUDE,
    "date" : date_string,
    "tzid" : "Europe/Berlin"
}

r = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
r.raise_for_status()
data = r.json()
print(f"Sunrise: {data["results"]["sunrise"]}")
print(f"Day Length: {data["results"]["day_length"]}")
print(f"Sunset: {data["results"]["sunset"]}")

#if iss close to my pos and its nighttime -> send email to look up, run code every 60 seconds on top!


