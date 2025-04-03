import smtplib
import datetime
import random
import time
import os

# Using a .env file to retrieve the phone numbers and tokens.

class NotificationManager:

    def __init__(self):
        self.gmail_app_password = os.getenv("XXXMAIL")
        self.from_email = "XXXX@gmail.com"
        
    def send_email(self, email_addr, message_body):
        """        
        Parameters:
        message_body (str): The text content of the email message to be sent.

        Returns:
        None

        Notes:
        Ensure that `APPMAIL` are correctly set up in your environment (.env file). GMail app key.      
        """
        
        email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
        email_connection.starttls()
        email_connection.login(user=self.from_email, password=self.gmail_app_password)
        
        email_connection.sendmail(from_addr=self.from_email, 
                                  to_addrs=email_addr, 
                                  msg=f"Subject:Low Price Flight Alert\n\n\n\n{message_body}")
    
        now = datetime.datetime.now()
         
        print(f"Price Alert Notice Sent: {now.month}/{now.day} @ {now.hour}:{now.minute}\n")

        email_connection.close()
        

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    # def send_whatsapp(self, message_body):
    #     message = self.client.messages.create(
    #         from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
    #         body=message_body,
    #         to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
    #     )
    #     print(message.sid)
