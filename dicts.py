product = {
    'name' : 'Iphone XS',
    'stock' : 5,
    'price' : 65000
}

print(product)
print('\n')

#Размер словаря
print('Размер словаря')
print(len(product))
print('\n')

#Добавление/изменение эллемента
print("Добавление элемента в словарь")
product['stock'] = 66 # изменили колличество
product['memory'] = 64 #добавили новый ключ
print(product)
print('\n')

#Обращение к отдельному элементу по ключу
print('Обращение к отдельному элементу по ключу')
print(product.get('name'))
print(product.get('discount'))#такого ключа нет
print(product.get('discount',0))#такого ключа нет, но вот тебе 0% скидки если ты так хочешь
print('\n')

#Удаление элементов
print('Удаление элементов')
del product['stock']
print(product)
print('\n')

#Объединение списков и словарей
print('Объединение списков и словарей')
phones_list = ['Xiaomi Mi8', 'iPhone Xs', 'Samsung Galaxy S10', 'iPhone Xs']
product['recomend'] = phones_list
print(product)
print('\n')

#Вложенный словарь
print('Работа с вложенным словарем')
product = {
    'name' : 'Iphone XS',
    'stock' : 5,
    'price' : 65000,
    'recomend' : phones_list,
}
print(product['recomend'])
print(product['recomend'][1])
#Добави эллемент в конец списка
product['recomend'].append('Motorola')
print(product)
print('\n')

#Список словарей
print('Список словарей')
stock = [
    {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
    {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
    {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
]
print('Просто вывод начального списка')
print(stock)
print('Вывод нулевого элемента списка, который является словарем')
print(stock[0])
stock[0]['price'] += 20000
print(stock[0])
print('\n')

#Обращение к вложенным данным
print('Обращение к вложенным данным')
print(stock[0]['recomended'][1])
print('\n')

#Выяснение типа данных
print('Выяснение типа данных')
print(type(stock[0]['recomended'][1]))
print(type(stock[0]['stock']))