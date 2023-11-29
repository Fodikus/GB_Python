# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

N = int(input("Введите натуральное число N: "))
array = []
for i in range(N):
    array.append(int(input(f"Введите число N{i+1}: ")))
print(' '.join(map(str, array)))

X = int(input("Введите число X, с которым необходимо сравнить числа массива: "))
found = array[0]
for item in array:
    if abs(item - X) < abs(found - X):
        found = item

print(f"Самое близкое к числу {X} в массиве является {found}" )