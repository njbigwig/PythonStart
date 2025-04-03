import smtplib
import datetime
import random
import time
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.gmail_app_password = os.getenv("XXXMAIL")
        self.from_email = "XXXX@gmail.com"
        
    def email_price_alert(self, to_email, alert_body):
        email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
        email_connection.starttls()
        email_connection.login(user=self.from_email, password=self.gmail_app_password)
        
        email_connection.sendmail(from_addr=self.from_email, 
                            to_addrs=to_email, 
                            msg=f"Subject:Low Price Flight Alert\n\n\n\n{alert_body}")
    
        now = datetime.datetime.now()
         
        print(f"Price Alert Notice Sent: {now.month}/{now.day} @ {now.hour}:{now.minute}")

        email_connection.close()
        
    