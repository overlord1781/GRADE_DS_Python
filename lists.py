#Импорт
import defs as ds
#Создание списка
ds.line_for_print()
print('Создане списка')
phones_list = ['Xiaomi Mi8', 'iPhone Xs', 'Samsung Galaxy S10', 'iPhone Xs', 'проверка коммита на гите']
phones_count = len(phones_list)
print(phones_list)
print(phones_count)
print('\n')

#Добавление эллементов
ds.line_for_print()
print('Добавление эллементов')
phones_list.append('Iphone 6')
phones_count = len(phones_list)
print(phones_list)
print(phones_count)
print('\n')

#Подсчет списка элементов
ds.line_for_print()
print('Подсчет элементов')
print(phones_list.count('Iphone 6'))
print(phones_list.count('Iphone 12'))
print('\n')

#Обращение по индексу
ds.line_for_print()
print('Обращение по индексу')
print(phones_list[0])
print('\n')

#Срезы
ds.line_for_print()
print('Срезы')
print(phones_list[1:3])
print(phones_list[-1])
print(phones_list[:2])
print('\n')

#Поиск индекса эллемента и сортировка
ds.line_for_print()
print('Поиск индекса и сортировка')
print(phones_list.index('iPhone Xs'))
phones_list.sort()
print(phones_list)
print('\n')

#Проверка на вхождение
ds.line_for_print()
print('Проверка на вхождение')
print('iPhone Xs' in phones_list)
print('IPhone Xs' in phones_list)
print('\n')

#Удаление
ds.line_for_print()
print('Удаление')
del phones_list[3]
print(phones_list)
phones_list.remove('iPhone Xs')
print(phones_list)
print('\n')

#Удаление элементов
ds.line_for_print()
print('Удаление')
list_pop = [0,1,2,3,4,5]
list_pop.pop(3)
print(list_pop)
print('\n')

#Удаление элементов
ds.line_for_print()
print('Удаление')
list_remove = [0,1,2,3,4,5]
list_remove.remove(2)
print(list_remove)
print('\n')

#Добавление одного списка к другому
ds.line_for_print()
print('Добавление одного списка к другому')
phone_brands = ['nokia', 'samsung', 'iphone', 'LG']
phone_brands.extend(phones_list)
print(phone_brands)
print('\n')

#Вставка элеемента на конкретный индекс списка
ds.line_for_print()
print('Вставка элеемента на конкретный индекс списка')
phone_brands.insert(0,'Emobile')
print(phone_brands)
print('\n')

#Развернуть список
ds.line_for_print()
print('Развернуть список')
list_reverse = [0,1,2,3,4,5,6,7,8,9]
list_reverse.reverse()
print(list_reverse)