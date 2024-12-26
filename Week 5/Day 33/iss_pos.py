import requests, datetime as dt

MY_LATITUDE = 49.319538
MY_LONGITUTE = 7.334330

time = dt.datetime.now()
if time.hour <= 8 or time.hour >= 17:
    check_iss(true)

def check_iss(is_night: bool):
    if is_night:
        r = requests.get("http://api.open-notify.org/iss-now.json")
        r.raise_for_status()
        data_iss = r.json()

        lat_iss = data_iss["iss_position"]["latitude"]
        long_iss = data_iss["iss_position"]["longitude"]

        if abs(MY_LATITUDE - lat_iss) <= 2 and abs(MY_LONGITUTE-long_iss) <= 2:
            send_mail()

def send_mail():