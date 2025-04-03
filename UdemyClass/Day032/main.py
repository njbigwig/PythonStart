import smtplib
import datetime
import random
import os

# App password stored securely as a ENV variable
gmail_app_password = os.getenv("XXX")

my_email = "xxxx@yyy.com"

email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
email_connection.starttls()
email_connection.login(user=my_email, password=gmail_app_password)

now = datetime.datetime.now()
day_of_week = now.weekday()

# print(type(now))
# print(f"{now.month} {now.day} {now.year}")
# print(f"{now.hour} {now.minute} {now.second} {now.microsecond}")

pastdate = datetime.datetime(year=1963, month=1, day=23)

quotelist = []
with open("quotes.txt") as quotefile:
    quotelist = quotefile.readlines()

random.shuffle(quotelist)

dailyquote = quotelist.pop(0)

if day_of_week == 0:
    # send email
    email_connection.sendmail(from_addr=my_email, 
                              to_addrs="xxx@x.com", 
                              msg=f"Subject:Greetings!\n\nHello World, from Python!\n\n{dailyquote}")
    
    print("Inspiring Daily Quote Sent...")

email_connection.close()

