import requests
from bs4 import BeautifulSoup


# URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL = "https://web.archive.org/web/20201117032952/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

# film_test = soup.find(name="div", class_="article-title-description__text")
# film_rank = film_test.find(name="h3", class_="title").getText()
# print(film_rank)

film_list = [film.getText() for film in soup.find_all(name="h3", class_="title")]
film_list.reverse()
# print(film_list)


# getting error with: '59) E.T. â\x80\x93 The Extra Terrestrial' -- , encoding="UTF-8"
with open(file="movies.txt", mode="w", encoding="UTF-8") as file:
    for film in film_list:
        file.write(f"{film}\n")
