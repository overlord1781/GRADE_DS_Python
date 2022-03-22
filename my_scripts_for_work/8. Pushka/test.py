import requests
import config
import json
# Согласно полученных list places ищем события 
null_events = []
with open ('./123.json', encoding='utf-8') as f:
    template = json.load(f)

'''
request_event = requests.get(f'https://pushka.gosuslugi.ru/api/v1/places/22677/events/', headers={'Authorization':config.TOKEN})
items = request_event.json()
if 'null' not in items:
    for i in items['data']:
        null_events.append(i['id'])

print(null_events)
'''


for i in template['data']:
    for key, value in i.items():
        if value == 'null': print(i['id'])