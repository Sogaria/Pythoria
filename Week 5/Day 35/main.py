import requests, json, twilio

api_key = "f26a29d7ed9d42b869059f1f2e7ad4cf"
lati = 47.32
longi = 8.33
api_call = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" : lati,
    "lon" : longi,
    "appid" : api_key,
    "cnt" : 4
}

r = requests.get(api_call, params=parameters)
r.raise_for_status()

data = r.json()

with open("weather_forecast.json", "w") as file:
    json.dump(data, file)

#check if its snowing in next 12 hours
for item in data["list"]:
    if item["weather"][0]["main"] == "Rain": 
        print("You will need an umbrella!")
        break
