##################################################        While       ##################################################
x = 1
while x < 5:
    print(x)
    x+=1
print('\n')

##################################################        While  Бесконечный цикл     ##################################################
while True:
    user_say = input('Скажи что нибудь \n')
    if user_say == 'Пока':
        print('До встречи')
        break
    else:
        print('Сам ты {}'.format(user_say))

print('\n')