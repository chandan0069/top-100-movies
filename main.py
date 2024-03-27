import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
top_movies_page = response.text

# print(top_movies_page)

soup = BeautifulSoup(top_movies_page, "html.parser")

movies_tags = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_names = []
for tag in movies_tags:
    name = tag.getText()
    movie_names.append(name)

movie_names = movie_names[::-1]

with open('movie_names.txt', 'w') as file:
    for movie_name in movie_names:
        file.write(movie_name + '\n')

# print(movie_names)