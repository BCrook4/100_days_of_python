from datetime import datetime, timezone

import requests

MY_LAT = 43.255587
MY_LONG = -79.879779

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
#
# iss_position = (latitude, longitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "EST"
}

response = requests.get("https://api.sunrise-sunset.org/json", params= parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

sunrise_hr = sunrise.split("T")[1].split(":")[0]
sunset_hr = sunset.split("T")[1].split(":")[0]
print(sunrise_hr)
print(sunset_hr)

# sunrise_list = sunrise.split(':')
# sunrise_list[0] = str(int(sunrise_list[0]) - 5)
# sunrise = ':'.join(sunrise_list)
#
# sunset_list = sunset.split(':')
# sunset_list[0] = str(int(sunset_list[0]) - 5)
# sunset = ':'.join(sunset_list)
# print(sunset)
# print(sunrise)

time_now = datetime.now()
print(time_now.hour)

