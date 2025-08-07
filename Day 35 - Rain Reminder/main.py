import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
api_key = os.getenv("OWM_API_KEY")
to_phone_number = os.getenv("TO_PHONE_NUMBER")
from_phone_number = os.getenv("FROM_PHONE_NUMBER")

parameters = {
    "lat": 38.845031,
    "lon": -77.308594,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

codes = [weather_data["list"][i]["weather"][0]["id"] for i in range(0, 4)]
print(codes)

will_rain = any(code < 600 for code in codes)
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=from_phone_number,
        body="It's going to rain today. Remember to take an ☔️",
        to=to_phone_number,
    )
    print(message.status)
