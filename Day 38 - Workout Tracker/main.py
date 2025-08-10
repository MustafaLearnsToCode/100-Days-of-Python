import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
API_ENDPOINT = os.getenv("API_ENDPOINT")

SHEETS_ENDPOINT = os.getenv("SHEETS_ENDPOINT")
EMAIL = os.getenv("EMAIL")
NAME = os.getenv("NAME")

stats = input("Enter your exercise details: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": stats,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(API_ENDPOINT, headers=headers, json=parameters)
data = response.json()
print(data)

for i in data["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%H:%M:%S"),
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"],

        }
    }

    response_sheets = requests.post(SHEETS_ENDPOINT, json=sheet_inputs)
    print(response_sheets.text)