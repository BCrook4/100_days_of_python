import os
import requests
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(".env.txt")

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_BEAR_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")

USERNAME = "bentoncrook3@gmail.com"
PROJECT_NAME = "workoutTracking"
SHEET_NAME = "workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_host_domain = "	https://trackapi.nutritionix.com"
exercise_language_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    # "query": exercise,
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 175,
    "age": 26,
}

exercise_params['query'] = input("What exercise did you do today?")

response = requests.post(url=exercise_language_endpoint, json=exercise_params, headers=headers)
response.raise_for_status()
data = response.json()

sheety_endpoint = "https://api.sheety.co/7213694a56b63c70dad9cbbc59b1138f/workoutTracking/workouts"

date = datetime.now()
date = date.strftime("%d/%m/%Y")
time = datetime.now().time()
time = time.strftime("%X")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEAR_TOKEN}"
}

for session in data['exercises']:

    row_data = {
        "workout":{
            "date": date,
            "time": time,
            "exercise": session['name'].title(),
            "duration": session['duration_min'],
            "calories": session['nf_calories'],
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json= row_data, headers=sheety_headers)
    sheet_response.raise_for_status()
    # print(sheet_response.text)

