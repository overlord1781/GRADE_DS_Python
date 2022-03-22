def line_for_print(value = 100):
    for i in range(value):
        print('-', end='')
    print()


product = {
    'name' : 'Iphone XS',
    'stock' : 5,
    'price' : 65000,
    'discount': 50
}

def discounted(price,discount, max_discount = 80):
    max_discount = abs(float(max_discount))
    price = abs(float(price))
    discount = abs(float(discount))
    if max_discount >=  90:
        raise ValueError('Ошибка по скидке!!!')

    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price-price*discount/100

    return price_with_discount

product['price_with_discounted'] = discounted(product['price'],product['discount'])
print(product)


def func1 (a, b , c=0):
    return print (a * b *c)
func1(1,2,3)
func1(1,2)

def func2 (*args):
    return print(sum(args))

func2(2,5,6,15,20)
func2()

def func3 (**kwargs):
    return print(kwargs)

print('\n')
print('Пример анонимной функции')
print((lambda x,y,z: (x+y)**z)(1,2,3))

print('\n')
print('Пример не анонимной функции')
f = lambda x,y,z: (x+y)**z
print(f(4,5,6))