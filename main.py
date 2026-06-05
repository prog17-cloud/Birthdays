##################### Hard Starting Project ######################

import pandas
import datetime as dt 
import random
import glob
import smtplib
import os
today = dt.datetime.now()
month = today.month
day=today.day
data = pandas.read_csv('birthdays.csv')
today_matches = data[(data["month"] == month) & (data["day"] == day)]
if not today_matches.empty:
    name = today_matches.iloc[0]["name"]
    template_list = glob.glob("letter_templates/*.txt") 
    letter=random.choice(template_list)
    with open(letter,'r')as file :
        content = file.read()
    updated_content= content.replace("[NAME]",name)

    

    receiver_email=today_matches.iloc[0]["email"]
    sender_email = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASS")

    



    with smtplib.SMTP("smtp.gmail.com", 587) as connection: 

        connection.starttls()
        connection.login(sender_email,password) 
        connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
       msg=f"Subject:Happy Birthday\n\n{updated_content}"
        )
    
    
    

         
    








