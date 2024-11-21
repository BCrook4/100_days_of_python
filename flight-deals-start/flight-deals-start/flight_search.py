import os
import requests
from datetime import datetime
import time
from dotenv import load_dotenv

load_dotenv(".env.txt")

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self._get_new_token()
        self.destination_data = {}

    def _get_new_token(self):

        header = {
             'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, data=body, headers=header)
        return response.json()['access_token']


    def get_destination_code(self, city):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"

        header = {
            'Authorization': f"Bearer {self._token}"
        }

        body = {
            'keyword': city,
            'max': 1,
            'include': "AIRPORTS",
        }

        response = requests.get(url=IATA_ENDPOINT, params=body, headers= header)
        response.raise_for_status()
        data = response.json()

        try:
            code = data['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city}.")
            return "Not Found"

        return code


    def get_flight_offers(self, destination_city_code, from_time, to_time, is_direct=True):

        header = {
            'Authorization': f"Bearer {self._token}"
        }

        body = {
            'originLocationCode': "YYZ",
            'destinationLocationCode': destination_city_code,
            'departureDate': from_time.strftime("%Y-%m-%d"),
            'returnDate': to_time.strftime("%Y-%m-%d"),
            'adults': 1,
            'nonStop': "true" if is_direct else "false",
            'currencyCode': "CAD",
            'max': 10,
        }

        response = requests.get(url=OFFERS_ENDPOINT, params=body, headers=header)
        response.raise_for_status()

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
