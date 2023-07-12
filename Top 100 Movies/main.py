from bs4 import BeautifulSoup
import requests


response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_link = response.text
soup = BeautifulSoup(movie_link ,"html.parser")

movie_titles = [movie_title.getText() for movie_title in soup.find_all(name="h3",class_="title")]
movie_titles.reverse()


with open('Movies.txt', "w") as data_file:
     data_file.writelines(movie_title +'\n' for movie_title in movie_titles)
