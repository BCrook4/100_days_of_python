import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv(".env.txt")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_BEAR_TOKEN = os.getenv("SHEETY_AUTH_TOKEN")
        self.prices_endpoint = os.getenv("PRICES_ENDPOINT")
        self.users_endpoint = os.getenv("USERS_ENDPOINT")

        self.sheety_headers = {
            "Authorization": f"Bearer {self.SHEETY_BEAR_TOKEN}"
        }

        self.destination_data = {}

    def get_sheet_data(self):
        response = requests.get(url=self.prices_endpoint, headers=self.sheety_headers)
        response.raise_for_status()
        data = response.json()
        # pprint(data)

        return data['prices']

    def update_city_codes(self):

        for city in self.destination_data:
            row_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }

            put_response = requests.put(url=f"{self.prices_endpoint}/{city['id']}", json=row_data, headers=self.sheety_headers)
            put_response.raise_for_status()
            # print(put_response.text)

    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint, headers= self.sheety_headers)
        response.raise_for_status()
        # print(response.json())
        return response.json()['users']