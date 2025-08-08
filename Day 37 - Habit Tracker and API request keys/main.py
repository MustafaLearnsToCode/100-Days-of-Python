import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

PIXELA_ENDPOINT = os.getenv("PIXELA_ENDPOINT")
USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(PIXELA_ENDPOINT, json=user_params)
print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(response.text)

graph_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}

response_pixel = requests.post(graph_pixel_endpoint, json=pixel_data, headers=headers)
print(response_pixel.text)

graph_put_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4",
}

response_pixel_put = requests.put(graph_put_endpoint, headers=headers, json=new_pixel_data)
print(response_pixel_put.text)

response_delete = requests.delete(graph_put_endpoint, headers=headers)
print(response_delete.text)