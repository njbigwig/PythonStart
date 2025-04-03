import requests
from requests.exceptions import RequestException
from datetime import datetime
import smtplib
import os
import json

def send_sms(mdn, message):
    # App password stored securely as a ENV variable
    gmail_app_password = os.getenv("XXXMAIL")

    my_email = "XXXX@gmail.com"   
    
    email_to = f"{mdn}@XXXX.com"
    
    email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    email_connection.starttls()
    email_connection.login(user=my_email, password=gmail_app_password)
    
    # send email
    email_connection.sendmail(from_addr=my_email, 
                            to_addrs=email_to, 
                            msg=f"Subject:Weather Alert\n\n{message}\n".encode("utf-8"))
    
    print(f"Sent text to MDN via VTEXT service: {mdn} : {email_to}")
    
    email_connection.close()

# API password stored securely as a ENV variable
api_app_key = os.getenv("XXXX_API")


#print("Weather by town name:")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?q=Snoqualmie&appid={api_app_key}", timeout=10)
response.raise_for_status()  # Check for HTTP errors
#print(response.json(),"\n")

#print("Weather by zipcode:")
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/weather?zip=98065,us&appid={api_app_key}", timeout=10)
response.raise_for_status()  # Check for HTTP errors
#print(response.json(),"\n")

XXXX_lat = response.json()["coord"]["lat"]
XXXX_long = response.json()["coord"]["lon"]

print(f"Home lat={XXXXX_lat} long={XXXXXX_long}")

#print("5 day Weather by lat-long:")
weather_parameters = {
    "lat": XXXXX_lat,
    "lon": XXXXXX_long,
    "cnt": 4,
    "appid": api_app_key
}
response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=weather_parameters, timeout=10)
response.raise_for_status()  # Check for HTTP errors
#print(response.json(),"\n")

pretty_json = json.dumps(json.loads(response.content), indent=2)
#print(pretty_json,"\n")

daily_weather = response.json()["list"]

# rain over the next 12 hours
will_rain = False 

for hour in daily_weather:
    #print(f"{hour["weather"]} {hour["weather"][0]["icon"]} {hour["dt_txt"]}")
    #print(f"{hour["weather"]}")
    
    condition_code = hour["weather"][0]["id"]
    
    # rainy weather condition
    if condition_code < 700:        
        will_rain = True
    

if will_rain == True:
    print("Bring your umbrella...") 
    send_sms("9999999999", "Bring your umbrella...")
    send_sms("9999999999", "Bring your umbrella...")
    
    
   
