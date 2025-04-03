import requests
import datetime

# pip install requests

MY_LAT = 0.0000
MY_LONG = -1.22222

iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')

iss_response.raise_for_status()




data = iss_response.json()
# print(data)

# iss_data_position = response.json()["iss_position"]
# print(iss_data_position)

iss_data_position_latitude = iss_response.json()["iss_position"]["latitude"]
#print(iss_data_position_latitude)

iss_data_position_longitude = iss_response.json()["iss_position"]["longitude"]
#print(iss_data_position_longitude)

iss_position = (iss_data_position_longitude, iss_data_position_latitude)
print(iss_position)

home_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/Los_Angeles"
}

sun_position_response = requests.get("https://api.sunrise-sunset.org/json", params=home_parameters)
sun_position_response.raise_for_status()
sun_position_data = sun_position_response.json()
sunrise = sun_position_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun_position_data["results"]["sunset"].split("T")[1].split(":")[0]
print(f"SUNRISE: {sunrise}")
print(f"SUNSET: {sunset}")
# print(sunrise.split("T")[1].split(":"))
# print(sunset.split("T")[1].split(":"))

time_now = datetime.datetime.now()
#print(time_now)
print(f"{time_now.hour}:{time_now.minute}")