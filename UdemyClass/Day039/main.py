#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# pip install amadeus

import requests
from requests.exceptions import RequestException
import datetime
import smtplib
import os
import json
import html
import flight_search
import data_manager
import notification_manager

FROM_AIRPORT="XXX"
TO_AIRPORT="YYY"

travel_date = input("Enter Travel Date (YYYY-MM-DD): ")

flightmananger = flight_search.FlightSearch(os.getenv("XXX"), os.getenv("XXXX_SECRET"))

datamanager = data_manager.DataManager()

notificationmanager = notification_manager.NotificationManager()

#print(f"Destinations: {datamanager.destination_count()}")
for dest in range(datamanager.destination_count()):
    dest_info = datamanager.destintation_info(dest)
    
    #print(dest_info)      
    print(f"Searching for flights from {FROM_AIRPORT} to {dest_info[0]} on {travel_date}")
    
    response = flightmananger.search_flights(FROM_AIRPORT, dest_info[0], travel_date)
    
    flightstr = ""
    for flight in response.data:    
        if float(flight["price"]["total"]) < dest_info[1]:
            flightstr = f"Only ${flight["price"]["total"]} Until: {flight["lastTicketingDate"]} {flight["validatingAirlineCodes"][0]} From: {FROM_AIRPORT} To: {dest_info[0]}\n "
            # segno = 1
            # for segment in flight["itineraries"][0]["segments"]:
            #     dt_object = datetime.datetime.strptime(segment["departure"]["at"], "%Y-%m-%dT%H:%M:%S")
            #     formatted_time = dt_object.strftime("%I:%M %p")
            #     flightstr = flightstr + f"Segment: {segno} {segment["carrierCode"]} {segment["number"]} Departing {segment["departure"]["iataCode"]} at {formatted_time} "
            #     segno += 1
                
    if flightstr != "":
        #print(flightstr,"\n")
        notificationmanager.email_price_alert("XXXX@gmail.com", flightstr)
        

# print(response.data)
# print(response.body)

# for flight in response.data:    
#     flightstr = f"${flight["price"]["total"]} {flight["lastTicketingDate"]} "
#     segno = 1
#     for segment in flight["itineraries"][0]["segments"]:
#         #print(segment)
#         dt_object = datetime.datetime.strptime(segment["departure"]["at"], "%Y-%m-%dT%H:%M:%S")
#         formatted_time = dt_object.strftime("%I:%M %p")
#         flightstr = flightstr + f"Segment: {segno} {segment["carrierCode"]} {segment["number"]} Departing {segment["departure"]["iataCode"]} at {formatted_time} "
#         segno += 1
        
    #print(flightstr,"\n")
        
    # print(f"Low Price Alert! Only ${flight["price"]["total"]} on {flight["validatingAirlineCodes"][0]} to fly from {FROM_AIRPORT} to {TO_AIRPORT} on 2025-09-04 until {flight["lastTicketingDate"]}")     
    
    # connections = len(flight["itineraries"][0]["segments"])
    # if connections > 1:
    #     print(f"Multiple Connections: {connections}")
    # else:
    #     print("Nonstop")
        
    # print("\n")
    
# notificationmanager.email_price_alert("xxxxxx@gmail.com", "Only $100 for a flight")
        



