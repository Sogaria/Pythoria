import requests, datetime as dt, smtplib, schedule, time
from geopy.geocoders import Nominatim

MY_LATITUDE = 49.319538
MY_LONGITUTE = 7.334330

my_email = "te2t3k53@gmail.com"
my_pw = "qcuf pbrg uvtk wycr"

def check_iss(is_night: bool):
    if is_night:
        r = requests.get("http://api.open-notify.org/iss-now.json")
        r.raise_for_status()
        data_iss = r.json()

        lat_iss = float(data_iss["iss_position"]["latitude"])
        long_iss = float(data_iss["iss_position"]["longitude"])

        if abs(MY_LATITUDE - lat_iss) <= 15 and abs(MY_LONGITUTE-long_iss) <= 9:
            print(f"ISS is close enough at ({lat_iss},{long_iss})")
            try: 
                geolocator = Nominatim(user_agent="geoapi")
                latitude = lat_iss
                longitude = long_iss
                location = geolocator.reverse((latitude, longitude))
                print(f"Currently at {location.address}")
            except AttributeError:
                print(f"Unknown location at ({lat_iss}, {long_iss})")
            send_mail()
        else:
            print(f"ISS is not close enough, currently at ({lat_iss}, {long_iss})")
            try:
                geolocator = Nominatim(user_agent="geoapi")
                latitude = lat_iss
                longitude = long_iss
                location = geolocator.reverse((latitude, longitude))
                print(f"Address: {location.address}")
            except AttributeError:
                print(f"Unknown location at {lat_iss}, {long_iss}")
    else:
        print("Right now its daytime at your location!")

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pw)
        connection.sendmail(from_addr=my_email, to_addrs="hackermaus@gmail.com", msg="Subject: ISS\n\nLook up!")

def check_time():
    time = dt.datetime.now()
    print(time)
    if time.hour <= 8 or time.hour >= 17:
        check_iss(True)

schedule.every(60).seconds.do(check_time)

while True:
    schedule.run_pending()
    time.sleep(1)
