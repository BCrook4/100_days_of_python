from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from datetime import datetime, timedelta
from notification_manager import NotificationManager
import time
from pprint import pprint

# used to save on api requests
from data_storage import sheetly_data, users_data

ORIGIN_CITY_IATA = "YYZ"

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()
# # commented out for now to save on API calls
# sheet_data = dataManager.get_sheet_data()
sheet_data = sheetly_data

# ========================== Update Airport Codes in Sheet =========================

if sheet_data[0]["iataCode"] == "":

    for row in sheet_data:
        row['iataCode'] = flightSearch.get_destination_code(row['city'])

dataManager.destination_data = sheet_data
# dataManager.update_city_codes()

# =========================== Get Customer Emails =================================
# users_data = dataManager.get_customer_emails()

emails = [user['email:'] for user in users_data]

# =========================== Search for Direct Flights ===========================
tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days= (6*30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flightSearch.get_flight_offers(
        destination_city_code=destination['iataCode'],
        from_time=tomorrow,
        to_time=six_months
    )

    cheapest_flight = find_cheapest_flight(flights)
    print(f"Cheapest flight to {destination['city']} is {cheapest_flight.price}")

    # =========================== Search for inDirect Flights ===========================
    is_direct = "direct"
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flightSearch.get_flight_offers(
            destination_city_code=destination['iataCode'],
            from_time=tomorrow,
            to_time=six_months,
            is_direct= False
        )
        is_direct = "indirect"

        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest flight to {destination['city']} is {cheapest_flight.price}")


    # Compare price to sheet and send text or email if cheap flight is found
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination['lowestPrice']:
        print(f"Lower price flight found to {destination['city']}!")


        message = (f"Low price alert! Only ${cheapest_flight.price} to fly {is_direct} with {cheapest_flight.stops} stops from"
                   f" {cheapest_flight.departure_airport} to {cheapest_flight.destination_airport},"
                   f" on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        # notificationManager.send_message(message_body=message)
        notificationManager.send_emails(email_list=emails, body= message)

    # slowing down requests to avoid rate limit
    time.sleep(2)






