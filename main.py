import os
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth


API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
basic = HTTPBasicAuth(USERNAME, PASSWORD)

GENDER = "male"
WEIGHT_KG = 50
HEIGHT_CM = 170
AGE = 15

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/cdbbf8bf45585a7efafc9fb83b135406/myWorkouts/workouts"

exercise_text = input("What exercises did you do?: ")

header = {
    'x-app-id': APP_ID,
    "x-app-key": API_KEY
}

nutritionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=header)
result = response.json()


now = datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%X")


for exercise in result["exercises"]:
    new_row = {
        "workout": {
          "date": date,
          "time": time,
          "exercise": exercise["name"].title(),
          "duration": round(exercise["duration_min"]),
          "calories": round(exercise['nf_calories']),
        }
    }
    request = requests.post(url=sheety_endpoint, json=new_row, auth=basic)
    
