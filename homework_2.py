from random import *
"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
# number = input('Введите вещественное число:\n')
# digits = 1
# if '.' in number:
#     digits = 10 ** len(number.split('.', 1))
# number = float(number) * digits
# total = 0
# while number > 0:
#     total += int(number % 10)
#     number = number // 10
# print(f'Сумма всех цифр вещественного числа равна {total}')

"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
# number = int(input('Введите число:\n'))
# kit = []
# for i in range(1, number+1):
#     total = 1
#     for j in range(1, i+1):
#         total *= j
#     kit.append(total)
# print(kit)
"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
"""
# number_n = int(input('Введите число n:\n'))
# list_sequences = []
# for i in range(1, number_n + 1):
#     list_sequences.append(round((1+1/i)**i, 2))
# print(f'Сумма {number_n} чисел последовательностью (1 + 1/n)^n равна {sum(list_sequences)}')
"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в 
файле file.txt в одной строке одно число.
"""
# number_n = int(input('Введите количество элементов:\n'))
# kit_digit = []
# for i in range(number_n):
#     kit_digit.append(randint(-number_n, number_n))
# print(kit_digit)
# with open('index_hw2.txt', 'w') as file:
#     for i in range(randint(2, number_n)):
#         file.write(str(randint(0, len(kit_digit)-1)) + '\n')
# work = 1
# with open('index_hw2.txt', 'r') as index:
#     for i in index:
#         work *= kit_digit[int(i)]
# print(f'Произведение элементов на указанных позициях в файле {work}')

"""
Реализуйте алгоритм перемешивания списка.
"""
counter = int(input('Введите размер списка:\n'))
list_number = []
for i in range(counter):
    list_number.append(randint(1, 100))
print(list_number)
for i in range(counter):
    index = randint(0, len(list_number)-1)
    list_number[i], list_number[index] = list_number[index], list_number[i]
print(list_number)
