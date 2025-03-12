import requests
from bs4 import BeautifulSoup

def print_news(news):
  for url, li in news.items():
    print(f"Заголовок: '{li[0]}'\nВремя: {li[1]}\nСсылка: {url}\n")
url = 'https://lenta.ru/'
# Отправка GET-запроса к указанному URL
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
  allNews = []
  news = {}
  soup = BeautifulSoup(response.content, 'html.parser')
  allNews = soup.findAll('a', class_='card-mini _topnews', href=True)
  for data in allNews:
    if data.find('h3') is not None:
      l = []
      l.append(data.find('h3').text)
      l.append(data.find('time').text)
      href_wurl = url + data['href']
      news[href_wurl] = l
  print_news(news)
  news.clear()
  keyword = input("Введите ключевые слова\n")
  for data in allNews:
    if data.find('h3') is not None:
      if keyword.lower() in data.find('h3').text.lower():
        l = []
        l.append(data.find('h3').text)
        l.append(data.find('time').text)
        href_wurl = url + data['href']
        news[href_wurl] = l
  print_news(news)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
