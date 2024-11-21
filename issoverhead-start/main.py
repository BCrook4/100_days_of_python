import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 43.255587
MY_LONG = -79.879779
EMAIL = "bcrookprog@gmail.com"
PASSWORD = "phatemtrjrpiozqk"

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
    else:
        return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "EST",
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if not (sunrise < time_now.hour < sunset):
        return True
    else:
        return False



#Your position is within +5 or -5 degrees of the ISS position.




# print(sunrise, sunset, iss_latitude, iss_longitude, time_now.hour)


while True:
    # print(is_overhead(), is_dark())
    if is_overhead() and is_dark():


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="bentoncrook3@gmail.com",
                msg="Subject:Look Up!\n\n"
                    "The ISS is above you. Try to find it"
            )
    time.sleep(60)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



