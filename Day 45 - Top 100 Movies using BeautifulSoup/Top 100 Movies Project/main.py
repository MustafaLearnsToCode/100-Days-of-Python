import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, features="html.parser")

movies = soup.find_all("h3", class_="title")

with open("movies.txt", mode="w") as file:
    for i in movies[::-1]:
        movie = i.get_text()
        file.write(f"{movie}\n")

#Adding my own twist
import random

with open("movies.txt") as file:
    movies = file.readlines()
    random_movie = random.choice(movies)
    print(f"Tonight's movie is: {random_movie}")