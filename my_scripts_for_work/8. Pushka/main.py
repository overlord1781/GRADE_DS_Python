import json
from os import times
import requests
import config
import All_places
import time

URL_ID_Region = 'https://pushka.gosuslugi.ru/api/v1/locales/'
URL_Places = 'https://pushka.gosuslugi.ru/api/v1/locales/7/places'        #### Всего мест судя по id 4451
URL_Events = 'https://pushka.gosuslugi.ru/api/v1/places/2914/events/'     #### Всего событий судя по id 

r = requests.get(URL_ID_Region, headers={'Authorization':config.TOKEN})

# Получение списка всех областей и регионов
regions = r.json()
list_regions = []
for region in regions['data']:
    list_regions.append(region['_id'])


# Получение списка всех мест 

list_places = []
dict_plces = dict()
for region in list_regions:
    request_place = requests.get(f'https://pushka.gosuslugi.ru/api/v1/locales/{region}/places', headers={'Authorization':config.TOKEN})
    items = request_place.json()
    for i in items['data']:
        list_places.append(i['id'])




# Согласно полученных list places ищем события 

null_events = []
for place in config.PLACES:
    request_event = requests.get(f'https://pushka.gosuslugi.ru/api/v1/places/{place}/events/', headers={'Authorization':config.TOKEN})
    items = request_event.json()
    for i in items['data']:
        for key, vallue in i.items():
            if vallue == 'null' or 'NULL' or None:
                null_events.append(i['id'])


null_events = []
req_itog = {}
errore_list = []
for place in All_places.PLACES:
    request_event = requests.get(f'https://pushka.gosuslugi.ru/api/v1/places/{place}/events/', headers={'Authorization':config.TOKEN})
    items = request_event.json()
    k = str(place)
    try:
        req_itog[k] = items['data']
        with open(f'./data/data {place}.json', 'w', encoding='utf-8') as f:
            json.dump(req_itog,f, ensure_ascii=False)
        req_itog = {}
    except KeyError:
        errore_list.append(place)

print(errore_list)







