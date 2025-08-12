import os
import requests

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:

    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_API_SECRET")
        self.token = self.get_token()

    def get_destination_code(self, city_name):
        headers = {
            'Authorization': f'Bearer {self.token["access_token"]}'
        }
        params = {
            'keyword': city_name,
            'max':2,
            'subType': 'CITY'
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=params)

        try:
            code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"No IATA code found for city: {city_name}")
            return "N/A"
        except KeyError:
            print(f"Unexpected response structure: {response.json()}")
            return "Not found"

        return code

    def get_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

    def flight_search(self):
        headers = {
            "authorization": f"Bearer {self.token['access_token']}",
        }

        search_parameters = {
            "originLocationCode": "IAD",
            "destinationLocationCode": "BBI",
            "departureDate": "2025-01-25",
            "adults": 1
        }

        response = requests.get(url=SEARCH_ENDPOINT, params=search_parameters, headers=headers)

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, is_direct=True):

        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self.token['access_token']}"}

        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
