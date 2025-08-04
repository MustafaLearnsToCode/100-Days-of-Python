from datetime import *
import pandas
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv") #create your own csv with name | email | year | month | day
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )

