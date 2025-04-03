import requests
from requests.exceptions import RequestException
from datetime import datetime
import smtplib
import os
import json
import html
import string

# Define allowed characters
allowed_characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

# Function to filter the string
def filter_string(input_string):
    return ''.join(char for char in input_string if char in allowed_characters)


STOCK = "XXX"
COMPANY_NAME = "XXXXX"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
# """
# TSLA: 🔺2%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# or
# "TSLA: 🔻5%
# Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
# Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
# """

def send_email(eaddress, message):
    # App password stored securely as a ENV variable
    gmail_app_password = os.getenv("XXXMAIL")

    my_email = "XXXl.com"   
    
    email_to = eaddress
    
    email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
    email_connection.starttls()
    email_connection.login(user=my_email, password=gmail_app_password)
    
      
    # send email
    email_connection.sendmail(from_addr=my_email, 
                              to_addrs=email_to, 
                              msg=f"Subject:Stock Alert\n\n{message}\n")
                              #msg=f"Subject:Stock Alert\n\n{message.encode("utf-8")}\n")
    
    print(f"Sent email stock alert to: {eaddress}")
        
    email_connection.close()

STOCK_UP_SYMBOL = " Up "
STOCK_DOWN_SYMBOL = " Down "

# Stock API password stored securely as a ENV variable
stock_app_key = os.getenv("XXX_API_KEY")

print(f"Stock Price Data for: {STOCK}")

stock_api_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_app_key
}

# stock_response = requests.get(url=f"https://www.alphavantage.co/query", params=stock_api_parameters, timeout=10)
# stock_response.raise_for_status()  # Check for HTTP errors
# stock_dictionary = stock_response.json()["Time Series (Daily)"]
# print(stock_response.json()["Time Series (Daily)"],"\n")

# # Use dictionary comprehension to convert stock dictionary into stock list
# stock_list = [(date, details['1. open'], details['4. close']) for date, details in stock_dictionary.items()]

stock_list=[
    ["2025-03-14", 0, "388.5600"],
    ["2025-03-13", 0, "378.7700"]
]

print(stock_list[0][0], stock_list[0][2])
print(stock_list[1][0], stock_list[1][2])

stock_price_day1 = float(stock_list[0][2])
stock_price_day2 = float(stock_list[1][2])

stock_difference = round(((stock_price_day1 - stock_price_day2)/stock_price_day2) * 100, 1)
print(f"{STOCK} Closing Price: Current ${stock_price_day1} Previous ${stock_price_day2} Difference={stock_difference}%\n\n")

#print(STOCK_UP_SYMBOL, STOCK_DOWN_SYMBOL)

# News API password stored securely as a ENV variable
news_app_key = os.getenv("XXX_API_KEY")

stock_indicator = "Flat"
if stock_difference > 2.00:
    stock_indicator = STOCK_UP_SYMBOL
elif stock_difference < -2.00:
    stock_indicator = STOCK_DOWN_SYMBOL
     

print(f"News for {STOCK} {stock_difference}% {stock_indicator}")
stock_alert_title = f"News for {STOCK} {stock_difference}% {stock_indicator}"

news_api_parameters = {
    "q": COMPANY_NAME,
    "from": stock_list[0][0],
    "to": stock_list[1][0],
    "sortBy": "popularity",
    "apikey": news_app_key
}

news_response = requests.get(url=f"https://newsapi.org/v2/everything", params=news_api_parameters, timeout=10)
news_response.raise_for_status()  # Check for HTTP errors
#print(news_response.json()["articles"])
    
print(f"Headline: {news_response.json()["articles"][0]["title"]}\nBrief: {news_response.json()["articles"][0]["description"]}\n")
stock_alert_news1 = html.unescape(f"Headline: {news_response.json()["articles"][0]["title"].encode("utf-8")}\nBrief: {news_response.json()["articles"][0]["description"].encode("utf-8")}\n\r")
 
print(f"Headline: {news_response.json()["articles"][1]["title"]}\nBrief: {news_response.json()["articles"][1]["description"]}\n")
stock_alert_news2 = filter_string(html.unescape(f"Headline: {news_response.json()["articles"][1]["title"].encode("utf-8")}\nBrief: {html.unescape(news_response.json()["articles"][1]["description"]).encode("utf-8")}\n\r"))

print(f"Headline: {news_response.json()["articles"][2]["title"]}\nBrief: {news_response.json()["articles"][2]["description"]}\n")
stock_alert_news3 = html.unescape(f"Headline: {news_response.json()["articles"][2]["title"].encode("utf-8")}\nBrief: {news_response.json()["articles"][2]["description"].encode("utf-8")}\n\r")

stock_message = f"{stock_alert_title}{stock_alert_news1}{stock_alert_news2}{stock_alert_news3}"
send_email("XXXX@gmail.com", stock_message)



