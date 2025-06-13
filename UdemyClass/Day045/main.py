from bs4 import BeautifulSoup
import lxml
import requests

# html_content = None

# with open("website.html", "r") as file:
#     html_content = file.read()
#     print(html_content)
    
# html_soup = BeautifulSoup(html_content, "html.parser")
# print(type(html_soup))
# print(html_soup.prettify())

# # now a Python object
# print(html_soup.title)
# print(html_soup.title.name)
# print(html_soup.title.string)

# # get the first element
# print(html_soup.a)
# print(html_soup.li)
# print(html_soup.p)

# all_anchor_tags = html_soup.find_all(name="a")
# # print the list
# print(all_anchor_tags)

# print(all_anchor_tags[0].name)
# print(all_anchor_tags[0].string)

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
    
# heading1 = html_soup.find(name="h1", id="name")
# print(heading1)

# section_heading = html_soup.find(name="h3", class_="heading")

# print(section_heading)
# print(section_heading.getText())

# company_url = html_soup.select_one(selector="p a")
# print(company_url.get("href"))

# name = html_soup.select_one(selector="#name")
# print(name)

# classes = html_soup.select(".heading")
# print(classes)

# grab data from a live website
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.title.getText())

# Me
first_anchor = soup.select_one(selector=".titleline a")
print(first_anchor)
print(first_anchor.get("href"))
print(first_anchor.getText())

# Instructor
anchors = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []

for anchor in anchors:
    article_text = anchor.getText()
    article_texts.append(article_text)
    article_link = anchor.get("href")
    article_links.append(article_link)

points = soup.find_all(name="span", class_="score")
article_points = []
for point in points:
    article_upvotes = point.getText()
    article_points.append(int(article_upvotes.split()[0]))
    
    
idx = 0
for points in article_points:
    print(f"{article_texts[idx]}|{article_links[idx]}|{article_points[idx]}")
    idx += 1
    
# find the index of the post with the highest points
max_points = max(article_points)
idx = article_points.index(max_points)
print(f"Highest Points: {max_points}")
print(f"Index for Highest Score: {idx}\n")

print(f"{article_texts[idx]}|{article_links[idx]}|{article_points[idx]}")




