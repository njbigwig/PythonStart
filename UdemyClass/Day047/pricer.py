import requests
import os
from bs4 import BeautifulSoup
import pprint
import smtplib
import datetime
import random
import time


def send_email(email_addr, message_body):
    
    gmail_app_password = os.getenv("XXX")
    from_email = "heheh@gmail.com"
    
    email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    email_connection.starttls()
    email_connection.login(user=from_email, password=gmail_app_password)
    
    email_connection.sendmail(from_addr=from_email, 
                                to_addrs=email_addr, 
                                msg=f"Subject:Amazon Item Low Price Alert\n\n\n\n{message_body}")

    now = datetime.datetime.now()
        
    print(f"Price Alert Notice Sent: {now.month}/{now.day} @ {now.hour}:{now.minute}\n")

    email_connection.close()


header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
          "Accept-Language": "Accept-Language: en-US"}

#URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B09J1TB35S?ref=ppx_yo2ov_dt_b_fed_asin_title"

# Write your code below this line 
response = requests.get(url=URL, headers=header)
response.encoding = "utf-8"
amazon_webpage = response.text

soup = BeautifulSoup(amazon_webpage, "html.parser")
print(soup.title.getText())
#print(soup.prettify())

price_symbol = soup.find(class_="a-price-symbol")
currency = price_symbol.getText()

price_dollar = soup.find(class_="a-price-whole")
dollars = price_dollar.getText()

price_cents = soup.find(class_="a-price-fraction")
cents = price_cents.getText()

float_price = float(f"{dollars}{cents}")
print(f"Cost: {currency}{float_price}")

if float_price < 70.00:
    send_email("hehehe@gmail.com", f"{soup.title.getText()}\n\n{URL}")
else:
    print("Price TOO high!")






