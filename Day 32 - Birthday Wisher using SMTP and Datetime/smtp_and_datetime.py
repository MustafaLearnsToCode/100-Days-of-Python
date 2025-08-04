from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
send_email= os.getenv("SEND_EMAIL")

with smtplib.SMTP("smtp.gmail.com") as connection: #creates connection using with to avoide closing
    connection.starttls() #secures connection by encrypting it
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=send_email,
                        msg="Subject:Hello\n\nThis is the body of my email"
    )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
if year == 2025:
    print("The big 25")
print(type(now))
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2001 ,month=1 ,day= 1)
print(date_of_birth)

