import smtplib
import datetime
import random
import time
import os

# App password stored securely as a ENV variable
gmail_app_password = os.getenv("XXMAIL")

my_email = "XXXX@gmail.com"

quotelist = []
with open("quotes.txt") as quotefile:
    quotelist = quotefile.readlines()

random.shuffle(quotelist)

while True:  

  
    now = datetime.datetime.now()
    
    while not (now.hour == 6 and now.minute == 0):
        now = datetime.datetime.now()
        print(f"{now.hour}:{now.minute}")
        time.sleep(0.5) 
        
    
    day_of_week = now.weekday()   
    

    
    email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    email_connection.starttls()
    email_connection.login(user=my_email, password=gmail_app_password)
    
    dailyquote = quotelist.pop(0)

    # send email
    email_connection.sendmail(from_addr=my_email, 
                            to_addrs="XXXX@gmail.com", 
                            msg=f"Subject:Daily Motivational Quote\n\n\n\n{dailyquote}\n\nLearning Python.")
    
    print(f"Inspiring Daily Quote Sent: {now.month}/{now.day} @ {now.hour}:{now.minute}AM")

    email_connection.close()
        
    time.sleep(25) 
    time.sleep(25) 
    time.sleep(25) 

