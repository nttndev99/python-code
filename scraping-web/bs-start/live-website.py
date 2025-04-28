from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articales = soup.find_all(name="a", class_="storylink")
articale_texts = []
articale_links = []
for artical_tag in articales:
    text = artical_tag.getText()
    articale_texts.append(text)
    link = artical_tag.get("href")
    articale_links.append(link)
    
article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(articale_texts[largest_index])
print(articale_links[largest_index])

# print(articale_texts)
# print(articale_links)
# print(article_upvotes)
