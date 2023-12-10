# Задача 17: 
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

from random import randint

lst1 = [1, 1, 2, 0, -1, 3, 4, 4] # задать список чисел вручную

lst2 = list() # задать пустой список
for i in range(5):
    n = int(input())
    lst2.append(n) # в цикле заполнить список числами вводом с клавиатуры

lst3 = [] # задать пустой список
for i in range(10):
    n = randint(1, 5)
    lst3.append(n) # в цикле заполнить список случайными числами
    
unique_list = []
print(lst3)
for elem in lst3:
    if elem not in unique_list:
        unique_list.append(elem)
print(len(unique_list)) # выводим количество уникальных элементов