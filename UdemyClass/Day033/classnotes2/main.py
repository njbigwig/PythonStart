import requests
from requests.exceptions import RequestException
from datetime import datetime
import tkinter
import smtplib
import os

MY_LAT = 88.999 # Your latitude
MY_LONG = -56.999 # Your longitude

iss_action = None

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "America/Los_Angeles"
}

def send_me_email():
    print("Sending ISS alert email")
    # App password stored securely as a ENV variable
    gmail_app_password = os.getenv("XXXMAIL")

    my_email = "XXXX@gmail.com"
    
    email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    email_connection.starttls()
    email_connection.login(user=my_email, password=gmail_app_password)
    
    # send email
    email_connection.sendmail(from_addr=my_email, 
                            to_addrs=my_email, 
                            msg=f"Subject:ISS Alert\n\n\n\nLook up, ISS is near!\n\nDave")
    
    email_connection.close()
    

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
def iss_check():
    global parameters
    
    print("Checking for ISS position...\n")
    
    # response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
    # response.raise_for_status()
    # data = response.json()
    
    data = None   
    
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
            response.raise_for_status()  # Check for HTTP errors
            break  # Exit loop on success
        except RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
        else:
            print("All attempts failed.")
            
    data = response.json()

    # Is my position is within +5 or -5 degrees of the ISS position.
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])    
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    
    # is it dark?
    if time_now.hour >= sunset:
        print("It is now dark in the XXX, YYA area\n") 
        print(f"XXXX {MY_LAT} {MY_LONG}")
        print(f"ISS {iss_latitude} {iss_longitude}")
        print(f"ISS latitude range: {iss_latitude-5} {iss_latitude+5}")
        print(f"ISS longitude range: {iss_longitude-5} {iss_longitude+5}")
        
        if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            print("ISS is near, look up!")   
            send_me_email() 
    
    
    window.after(60000, iss_check)


window = tkinter.Tk()
window.title("ISS Spotter")
window.config(padx=50, pady=50)

iss_action = window.after(60000, iss_check)


            
window.mainloop()



