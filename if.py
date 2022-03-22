print('\n')
###############
balance = 10

print((balance<0))

if balance < 0:
    print('пополните баланс')
##############
print('\n')
##############
balance = 100
price = 200

print(bool(balance < 0 or price > balance))

if balance < 0 or price > balance:
    print('пополните баланс')
################################################ if + else ##################################
print('\n')

balance = 1000
price = 200

if balance > price :
    print('Спасибо за покупку')
else:
    print('Пополните баланс')

print('\n')
################################################ if + elif ####################################

temperature = 15

if temperature < 0:
    print('На улице холодно!')
elif 0 <= temperature <= 15: # Так как везде стоит знак <= то при выборе 15 градусов условие выполнится на первом вхождени и дальше не пойдет
    print('На улице холодок')
elif 15 <= temperature <= 25:
    print('На улице тепло')
else:
    print('Жара!!!')

print('\n')
################################################ обернем if в функцию ####################################

def weather(temperature):

    if temperature < 0:
        return 'На улице холодно!'
    elif 0 <= temperature <= 15:
        return 'На улице холодок'
    elif 15 <= temperature <= 25:
        return 'На улице тепло'
    else:
        return 'Жара!!!'

print(weather(8))
print(weather(28))
print(weather(-15))

print('\n')
################################################ обернем if в функцию 2 часть iPhone ####################################

phone1 = {'name': 'iPhone Xs Plus',
        'stock': 24,
        'price': 65432.1,
        'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10',
        'stock': 8,
        'price': 50000.0,
        'discount': 10}

def discounted(price , discount, max_discount=20, name = ''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
        raise ValueError('Ошибка по сумме скидки')
    elif discount > max_discount or 'iphone' in name.lower():
        return price
    else: return price -(price*discount/100)

apple_desc = discounted(phone1['price'], phone1['discount'], name = phone1['name'])
print(apple_desc)
apple_desc = discounted(phone2['price'], phone2['discount'], name = phone2['name'])
print(apple_desc)
print('\n')
################################################ отрицательные условия ####################################

phone1 = {'name': 'iPhone Xs Plus',
        'stock': 24,
        'price': 65432.1,
        'discount': 15}
phone2 = {'name': 'Samsung Galaxy S10',
        'stock': 8,
        'price': 50000.0,
        'discount': 10}
phone3 = {'name': '',
        'stock': 50,
        'price': 5000.5,
        'discount': 20}

def discounted2(price , discount, max_discount=20, name = ''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
        raise ValueError('Ошибка по сумме скидки')
    elif discount > max_discount or 'iphone' in name.lower() or not name: # просто проверка на пустую строку в списке ///or not name/// phone2 = {'name': '',
        return price
    else: return price -(price*discount/100)

apple_desc = discounted2(phone3['price'], phone3['discount'], name = phone3['name'])
print(apple_desc)
print('\n')