import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
SAMPLE_URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B0C6YP7288"
AMAZON_LINK = "https://www.amazon.com/Bleacher-Creatures-Angeles-Lakers-Lebron/dp/B0C6YP7288?sr=8-6"
TARGET_PRICE = 40
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")

headers = {
    "User-Agent": ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/139.0.0.0 Safari/537.36"),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.amazon.com/",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
}

response = requests.get(URL, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")
pprint(soup)

price_big = soup.find("span", class_="a-price-whole").get_text().split(".")[0]
price_small = soup.find("span", class_="a-price-fraction").get_text()
price = float(f"{price_big}.{price_small}")

#Used for cleaning product name in sample website
# product_name = soup.find("span", id="productTitle").get_text().strip().split("   ")
# clean_name = " ".join(item.strip() for item in product_name if item.strip())

name = soup.find("span", id="productTitle").get_text().strip()

if price <= TARGET_PRICE:
    with smtplib.SMTP(SMTP_SERVER, port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:AMAZON PRICE ALERT!\n\n{name} is now ${price}.\n{AMAZON_LINK}".encode("utf8")
                            )
