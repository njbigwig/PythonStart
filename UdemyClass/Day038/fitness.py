import requests
from requests.exceptions import RequestException
import datetime
import smtplib
import os
import json
import html


# get - retrieve rows:
# https://api.sheety.co/XXXXX/workoutTracking/workouts

# post - add a row:
SHEETY_URL = "https://api.sheety.co/XXXX/workoutTracking/workouts"

# put - edit a row:
# https://api.sheety.co/XXXXX/workoutTracking/workouts/[Object ID]

NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_api_id = os.getenv("XXXX_API_ID")
nutritionix_api_key = os.getenv("XXXXX_API_KEY")

print(nutritionix_api_id, nutritionix_api_key)

# Authentication
nutritionix_headers = {
    "x-app-id": nutritionix_api_id,
    "x-app-key": nutritionix_api_key
}

nutritionix_exercise_parameters = {
    "query": input("Exercise details: ")
}

data = None  

for attempt in range(3):  # Retry up to 3 times
    try:
        response = requests.post(url=NUTRITIONIX_URL, json=nutritionix_exercise_parameters, headers=nutritionix_headers, timeout=10)
        response.raise_for_status()  # Check for HTTP errors
        break  # Exit loop on success
    except RequestException as e:
        print(f"Post Attempt {attempt + 1} failed: {e}")
    else:
        print("All attempts failed.")
        
data = response.json()["exercises"]
# print(f"Exercise Types: {len(data)}\n\n")
# print(f"Exercise: {data[0]}\n\n")
# print(f"Exercise: {data[1]}\n\n")




SHEETY_TOKEN = os.getenv(XXXXTOKEN")
sheety_auth_header = {
    # Authorization: Bearer 3498gkvoFLKK^^&U*(ewuiieuiwerKJDEWIn
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

for exercise in data:
    tds = datetime.datetime.now()
    tdstime = tds.strftime("%H:%M:%S")
    tdsdate = tds.strftime("%m/%d/%Y")
    print(tdstime, tdsdate)

    print(f"{exercise["user_input"]} {exercise["duration_min"]} {exercise["nf_calories"]}")
    
    sheety_parameters = {
        "workout": {
            "date": tdsdate,
            "time": tdstime,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]        
        }
    }  
    
    edata = None   
    
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.post(url=SHEETY_URL, json=sheety_parameters, headers=sheety_auth_header, timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            break  # Exit loop on success
        except RequestException as e:
            print(f"Post Attempt {attempt + 1} failed: {e}")
        else:
            print("All attempts failed.")
            
    edata = response.json()
    print(f"User: {edata} {response} {response.text}\n\n") 
    


		
