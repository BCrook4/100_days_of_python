import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


# this is a workaround to save environmental variables
load_dotenv("C:/Users/bento/OneDrive/Documents/Programming/Python/EnvironmentalVariables/.env.txt")

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
api_key = os.getenv("OWM_API_KEY")

LAT = 43.26
LONG = -79.88

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": api_key,
    "cnt": 4,
}

# account_sid =
auth_token = os.getenv("AUTH_TOKEN")



response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for time in data["list"]:
    # print(time["weather"][0]["id"])
    # if time["weather"][0]["id"] < 700:
    #     will_rain = True
    condition_code = time["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # print("It's going to rain today. Bring a raincoat")
    client = Client(account_sid, auth_token)
    message = client.messages.create(

        body="It's going to rain today. Bring a raincoat.",

        from_="+17073293978",

        to="+15195253821",

    )
    print(message.status)
