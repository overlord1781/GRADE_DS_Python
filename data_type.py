import datetime
#Целые числа
print('Целые числа')
a = 6
b = 3
c = a + b
print(c)
print('\n')

#Вещественные числа
print('Вещественные числа')
a = 2.5
b = 0.5
c = a - b
print(c)

a = 2.5
b = 0.5
c = a / b
print(c)
print('\n')
#Логические типы

print('Логические типы')
a = 3
b = 2
c = b != a
print(c)
print('\n')
#Строковые типы

print('Строковые типы')
a = "Hello"
b = 'World'
d = 2
print(a+b)
print(a+' '+b+'!')
c = '{} {} {}!'.format(a,b,d)
print (c)

user = "Python"
c = 'Привет {name}!'.format(name = user)
print(c)

user = 'Python'
c = f'Привет {user}!'
print(c)
print('\n')

#Длина строки
print('Длина строки')
a = "Привет"
b = "Мир"
с = f"{a} {b}!"
d = len(c)
print(d)
print('\n')

# Приведение заглавных/строчных букв
print('Приведение заглавных/строчных букв')
d = c.upper()
print(d)
d = c.lower()
print(d)
d = c.capitalize()
print(d)
storka_s_probelami= "    PYThoN"
d = storka_s_probelami.strip().capitalize()
print(d)
print('\n')
# Замена символов в строках

print(' Замена символов в строках')
a = 'Прив3333т'.replace('3','е')
print(a)
a = 'ПриветЫ'.lower().replace('ы','').capitalize()
print(a)
print('\n')

# Подсчет слов в предложении
print('Подсчет слов в предложении')
a = 'Это очень длиное предложение и в нем есть ошибки, так как пишу на Немецкой клавиатуре, нткогда не покупайте ноутбук у немцев'
print(len(a.split()))
print('\n')
#None

a = None
b = 0

print(a is None)
print(b is None)
print(b is not None)
print('\n')

# Определение типа переменных
print('Определение типа переменных')
a = [1, 2.5, 'sdsd0', 23+4j, True]
i = 0
while i < len(a):
    print(type(a[i]))
    i+=1
print('\n')

# Ввод пользователем
print('Ввод пользователем')
name = input('Ввежите ваше имя: ')
print(f'Привет {name}!')

age = int(input('Сколько вам лет?'))
was_born = datetime.date.today().year-age
print(f'вы родились в {was_born} году ')