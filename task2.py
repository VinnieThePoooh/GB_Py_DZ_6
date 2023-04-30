# Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

len_1 = int(input('Введите длинну массива: '))
mini = int(input('Введите минимальное значение: '))
maxi = int(input('Введите максимальное значение: '))
list_1 = [random.randint(0,101) for i in range (len_1)]
print('Сгенерированный список: ', list_1)

for i in range(len(list_1)):
    if list_1[i] > mini and list_1[i] < maxi:
        print(i, end=' ')