##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime
import random
import os
import pandas

print("Birthday Wisher!\n\n")

bdaydata = pandas.read_csv("birthdays.csv")
#print(bdaydata)

letter1 = []
with open("letter_templates\\letter_1.txt") as letterfile:
    letter1 = letterfile.readlines()
#print(letter1)

letter2 = []
with open("letter_templates\\letter_2.txt") as letterfile:
    letter2 = letterfile.readlines()
#print(letter2)

letter3 = []
with open("letter_templates\\letter_3.txt") as letterfile:
    letter3 = letterfile.readlines()
#print(letter3)

now = datetime.datetime.now()
day_of_week = now.weekday()

print(f"Today is {now.month}/{now.day}\n")

# select a random letter template
letternumber = random.randrange(1,4)

if letternumber == 1:
    lettercontents = letter1 
elif letternumber == 2:
    lettercontents = letter2
else:
    lettercontents = letter3

for (index, row) in bdaydata.iterrows():
    #print(f"Name={row.Name} {row.Email} {row.Month}/{row.Day}/{row.Year}") 
   
    if now.month == row.Month and now.day == row.Day:
        print(f"Sending {row.Name} a birthday email #{letternumber}!\n")
        
        # App password stored securely as a ENV variable
        gmail_app_password = os.getenv("XXMAIL")

        my_email = "XXX@gmail.com"
        
        # Combine the letter template into a single string
        lettercontents = ''.join(lettercontents)
        
        customlettercontents = lettercontents.replace("[NAME]", row.Name)
        print(customlettercontents)

        email_connection = smtplib.SMTP("smtp.gmail.com", port=587)
        email_connection.starttls()
        email_connection.login(user=my_email, password=gmail_app_password)
        
        email_connection.sendmail(from_addr=my_email, 
                                  to_addrs=row.Email, 
                                  msg=f"Subject:On Your Birthday\n\n{customlettercontents}")
        
        email_connection.close()



 
    
    




