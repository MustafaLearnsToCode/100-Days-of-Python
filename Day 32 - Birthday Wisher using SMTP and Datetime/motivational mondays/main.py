import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SEND_EMAIL = os.getenv("SEND_EMAIL")

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,
                                to_addrs=SEND_EMAIL,
                                msg=f"Subject:Monday Motivation\n\nHere is your motivation quote for the day:\n{random_quote}")
