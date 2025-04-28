from bs4 import BeautifulSoup


with open("./web-project/bs-start/website.html") as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, "html.parser")
# print(soup)

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
    
# for tag in all_anchor_tags:
    # print(tag.get_text)
    
# heading = soup.find(name="h1", id="name")
# print(heading)

# h3_heading = soup.find(name="h3", class_="heading")
# print(h3_heading)

# url = soup.select_one(selector="#name")
# print(url)

headings = soup.select(".heading")
print(headings)