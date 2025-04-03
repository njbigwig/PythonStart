import amadeus
import requests
from requests.exceptions import RequestException
import datetime
import smtplib
import os
import json
import html



FLIGHT_AUTH_URL="https://test.api.amadeus.com/v1/security/oauth2/token"

flight_auth_param = {
    "grant_type": "client_credentials",
    "client_id": os.getenv("XXX_KEY"),  
    "client_secret": os.getenv("XXX_SECRET")  
}

flight_auth_header = {
    "Content-Type": "application/x-www-form-urlencoded"
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, apikey, apisecret):
        self.amadeus_id = amadeus.Client(client_id=apikey, client_secret=apisecret)
        
    def search_flights(self, fromairport, toairport, traveldate):
        response = self.amadeus_id.shopping.flight_offers_search.get(
                   originLocationCode=fromairport,
                   destinationLocationCode=toairport,
                   departureDate=traveldate,
                   currencyCode='USD',
                   adults=2)
        
        return response
        