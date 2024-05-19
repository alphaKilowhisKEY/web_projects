'''
Web Scraping Movie Titles

This Python script scrapes movie titles and saves them to a text file.

Prerequisites:
- Python 3.x
- BeautifulSoup (bs4)
- requests

Usage:
1. Modify the URL variable in the script to specify the URL of the webpage containing the movie titles.
2. Run the script:
$ python3 main.py
3. The script will create a file named movie_list.txt containing the scraped movie titles.

'''

from bs4 import BeautifulSoup
import requests


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
article_text_list = []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all(name="h3", class_="title")

    with open("movie_list.txt", mode="w") as file:

        for number, article in enumerate(articles, start=1):
            movie_name = ' '.join(article.getText().split()[1:])
            movie_list = file.write(f"{number})" + movie_name + "\n")

else:
    print("Response error.")     