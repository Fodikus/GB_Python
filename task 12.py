# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

x = int(input('Введите первое натуральное число X от 1 до 1000: '))
while x > 1000 or x <= 0:
    x = int(input("Вы ошиблись!\nВведите первое натуральное число X от 1 до 1000: "))

y = int(input('Введите второе натуральное число Y от 1 до 1000: '))
while y > 1000 or y <= 0:
    y = int(input("Вы ошиблись!\nВведите второе натуральное число Y от 1 до 1000: "))

stop = 0
for i in range(x):
    if stop != 1:
        for j in range(y):
            if stop != 1:
                if x == i + j and y == i * j:
                    print(f"Первое задуманное число: {i}, второе задуманное число: {j}.")
                    stop = 1