from bs4 import BeautifulSoup
import requests

sahifa = 'https://cbu.uz/uz/'
r = requests.get(sahifa)

soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_='exchange__item_value')
print(news[0].text)