from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
webpage = response.text
soup = BeautifulSoup(webpage, features="html.parser")

articles = soup.find_all("a", class_="storylink")
article_texts = []
article_links = []
for i in articles:
    article_text = i.get_text()
    article_texts.append(article_text)
    article_link = i.get("href")
    article_links.append(article_link)
    article_id = i.find("tr", class_="athing").get("id")
    article_upvote = soup.find("span", id=f"score_{article_id}").get_text()
    print(article_upvote)
