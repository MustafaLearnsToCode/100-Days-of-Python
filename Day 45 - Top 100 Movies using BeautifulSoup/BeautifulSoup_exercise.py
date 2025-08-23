from bs4 import BeautifulSoup
#import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") #can use lxml depending on website

print(soup.title) #can find specific tags
print(soup.title.name) #can find specific tag names
print(soup.title.string) #can find what's inside the tag
print(soup.prettify()) #pretty print the whole html with indentation
print(soup.a) #finds the first <a> tag
print(soup.p) #finds the first <p> tag
anchor_tags = soup.find_all("a") #finds all <a> tags in a list

for i in anchor_tags:
    print(i.get_text()) #prints the text inside each <a> tag
    print(i.get("href")) #prints the value of the href attribute

heading = soup.find(name="h1", id="name") #finds the first <h1> tag with id="name"
print(heading.get_text())

section_heading = soup.find(name="h3", class_="heading") #finds the first <h3> tag with class="heading"
print(section_heading.name) #NOTE: class is a reserved keyword in Python, so we use class_ instead

company_url = soup.select_one(selector="p a") #finds the first <a> tag inside a <p> tag
print(company_url.get_text())

name = soup.select_one(selector="#name") #finds the first <a> tag inside a <p> tag
print(name.get_text())

headings = soup.select(".heading") #finds all elements with class="heading"
print(headings)


