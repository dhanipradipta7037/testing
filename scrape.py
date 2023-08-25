import requests
from bs4 import BeautifulSoup
import time

data = []
for x in range(1, 6):
    time.sleep(5)
    url = f'https://books.toscrape.com/catalogue/page-{x}.html'
    respon = requests.get(url)
    parser = BeautifulSoup(respon.text, 'html.parser')
    items = parser.find_all('article', {'class':'product_pod'})
    for item in items:
        title = item.find('img', {'class':'thumbnail'}).get('alt')
        list_title = {'Title':title}
        data.append(list_title)
    time.sleep(5)

for x in data:
    print(x)