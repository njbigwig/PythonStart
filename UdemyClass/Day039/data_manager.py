import requests
from requests.exceptions import RequestException
import datetime
import smtplib
import os
import json
import html

SHEETY2_URL = "https://api.sheety.co/XXXXXXX/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.travel_list = []
        
        self.SHEETY_TOKEN = os.getenv("XXXX2")
        
        self.sheety_auth_header = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }
        
        self.sheety_response = requests.get(url=SHEETY2_URL, headers=self.sheety_auth_header)
        
        self.sheety_data = self.sheety_response.json()
        #print(self.sheety_data["prices"])
        
        self.travel_list = self.sheety_data["prices"]
        
    def destination_count(self):
        return len(self.travel_list)
   
    def destintation_info(self, idx):
        return (self.travel_list[idx]["iataCode"], float(self.travel_list[idx]["lowestPrice"]))