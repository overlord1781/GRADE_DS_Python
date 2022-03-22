import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
import pandas as pd


url = 'https://badaevsky.com/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

# Получаем список ссылок с главной страницы
list_urls = []
for i in soup.findAll('a'):
    link = str(i.get('href'))
    list_urls.append(link)

uniq_list_links = list(OrderedDict.fromkeys(list_urls).keys())
links_of_pages = []
count = 1
for x in list_urls:
    get_x = requests.get(url + x)
    bsoup = BeautifulSoup(get_x.text, 'lxml')
    all_hrefs = bsoup.findAll('a')
    for link in all_hrefs:
        if link not in uniq_list_links:
            links_of_pages.append(url + str(link.get('href')))
            print(count)
            count += 1
        else:
            continue

links_of_pages = list(set(links_of_pages))
links_404 = []
print(len(links_of_pages))
count = 1
for link in links_of_pages:
    r = requests.get(link)
    if 400 <= int(r.status_code) < 500 :
        links_404.append(link)
        print(count)
        count+=1

df = pd.DataFrame(links_of_pages)
df.to_excel('url.xlsx')
print("ready_urls")
df = pd.DataFrame(links_404)
df.to_excel('url-404.xlsx')
print("ready_404")