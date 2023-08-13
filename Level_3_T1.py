import requests
from bs4 import BeautifulSoup

url = 'https://www.bbc.com/news'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

article_titles = soup.find_all('h3', class_='gs-c-promo-heading__title')

for title in article_titles:
    print(title.get_text())
