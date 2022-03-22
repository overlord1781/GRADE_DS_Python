#######################################################################################
print('ПРИМЕР 1')
def cut_cake(people):
    try:
        parts = 1/people
        print(f'каждый получит {parts} пирога')
    except ZeroDivisionError:
        print('На ноль не делят')
    except TypeError:
        print('Вы ввели не чилсо людей')

cut_cake(0)
cut_cake('sdsd')
print('\n')
#######################################################################################
print('ПРИМЕР 2')
def cut_cake(people):
    try:
        parts = 1/people
        print(f'каждый получит {parts} пирога')
    except (ZeroDivisionError, TypeError):
        print('не могу делить проверьте вводимые данные')

cut_cake(5)
cut_cake('sdsd')
print('\n')
#######################################################################################
print('ПРИМЕР 3')
import random
def cut_cake(people):
    try:
        parts = 1/people
        print(f'каждый получит {parts} пирога')
    except:
        print('не могу делить проверьте вводимые данные')

