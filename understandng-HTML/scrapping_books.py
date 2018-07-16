import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.amazon.in')

soup = BeautifulSoup(page.content,'html.parser')

title = soup.find('title').string
print(title)