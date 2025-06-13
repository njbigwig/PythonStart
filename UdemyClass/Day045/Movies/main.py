import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
response.encoding = "utf-8"
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
print(soup.title.getText())
#print(soup.prettify())

movies = soup.find_all(name="h3", class_="title")

# print(movies)
top_100_list = []
for movie in movies:
   movie_text = movie.getText()
   top_100_list.append(movie_text)
   print(movie_text)
   
# can also reverse list via slice: [::-1]
idx = 99
with open("movies.txt", mode='w',  encoding='utf-8') as f:
    while idx >= 0:
        print(top_100_list[idx])
        f.write(top_100_list[idx])
        f.write("\n")
        idx -= 1
   

    




