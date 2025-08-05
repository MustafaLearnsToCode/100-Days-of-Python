import requests
from datetime import datetime

MY_LAT = 38.846226
MY_LNG = -77.306374

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code) #200 code = successful

#inefficient way to find status codes
if response.status_code == 404:
    raise Exception("that resource doesn't exist")
if response.status_code == 401:
    raise Exception("...")

#raise status code
response.raise_for_status()

#using json
data = response.json()

#specifically finding info in json and creating tuple
longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
iss_position = (float(longitude),float(latitude))

print(iss_position)

#parameters
parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted": 0,
}

response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data2 = response2.json()
sunrise = data2["results"]["sunrise"]
sunset = data2["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0]) #comparing specific hour

time_now = datetime.now()
print(time_now.hour)