import os
import requests
from requests.auth import HTTPBasicAuth


SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/XXX/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/XXXXXXXX/flightDeals/users"


class DataManager:

    def __init__(self):
        self._user = os.getenv("XXX_USRERNAME")
        self._password = os.getenv("XXXX_PASSWORD")
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.destination_data = {}
        self.email_list = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()  
        self.destination_data = data["prices"]
        return self.destination_data

    def get_customer_emails(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        self.email_list = data["users"] 
        print(f"customer emails: {self.email_list}\n")
        return self.email_list
    
    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
