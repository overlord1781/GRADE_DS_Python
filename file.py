#Открытие на чтение
f1 = open('text.txt', 'r')
print(f1.read(100))

#Открытие на запись
f2 = open('text2.txt', 'w')
f2.write(f1.read())
f1.close()
f2.close()

a = [1, 2, 3, 4, 5, 5]
with open('text.txt', 'a', encoding='utf-8') as file:
    for i in a:
        file.write('\n'+ str(i))
