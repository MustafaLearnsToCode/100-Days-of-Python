import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")

STOCK_APIKEY = os.getenv("STOCK_APIKEY")
NEWS_APIKEY = os.getenv("NEWS_APIKEY")

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

FROM_PHONE_NUMBER = os.getenv("FROM_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_APIKEY
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()
stock_list = [value for (key,value) in stock_data["Time Series (Daily)"].items()]
yesterday_data = stock_list[0]
yesterday_price = float(yesterday_data["4. close"])
print(yesterday_price)

day_before_data = stock_list[1]
day_before_price = float(day_before_data["4. close"])
print(day_before_price)

abs_difference = abs(yesterday_price - day_before_price)
print(abs_difference)

perc_difference = round(((abs_difference/day_before_price) * 100), 2)
print(perc_difference)

if perc_difference >= 0.05:
    news_parameters = {
        "q": COMPANY_NAME,
        "language": "en",
        "apiKey": NEWS_APIKEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    first_three_articles = news_data["articles"][:3]
    print(first_three_articles)

    formatted_text = [
        (f"{STOCK_NAME}: {'🔺' if yesterday_price > day_before_price else '🔻'}" f"{perc_difference}%"
         f"\nHeadline: {article['title']}\nBrief: {article['description']}") for article in first_three_articles]

    for i in range(0, 3):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            from_=FROM_PHONE_NUMBER,
            body=f"{formatted_text[i]}",
            to=TO_PHONE_NUMBER,
        )