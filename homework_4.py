'''
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

# accuracy, number = int(input('Enter accuracy: ')), float(input('Enter number: '))
# accuracy = len(str(accuracy).split('.')[1])
# number = (number * 10 ** accuracy // 1) / 10 ** accuracy
# print(f'{number:.{accuracy}f}')

'''
Задайте натуральное число N. Напишите программу, 
которая составит список простых множителей числа N.
'''
from sympy import *
# number = int(input('Enter number: '))
# simple_multipliers = []
# i = 2
# while i * i <= number:
#     while number % i == 0:
#         simple_multipliers.append(i)
#         number = number // i
#     i += 1
# if number > 1:
#     simple_multipliers.append(number)
# print(f'Simple multipliers of the number: {simple_multipliers}')

# Через библиотеку

# print(factorint(number))

'''
Задайте последовательность чисел. Напишите программу, которая 
выведет список неповторяющихся элементов исходной последовательности.
'''
# numbers = input('Enter the numbers through the gap: ')
# some_list = set()
# numbers_list = numbers.split(' ')
# for i in range(len(numbers_list)):
#     some_list.add(int(numbers_list[i]))
# print(some_list)

'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
'''
from random import *
natural_degree = int(input('Enter the degree: '))
coefficients = [randint(0, 100) for i in range(natural_degree + 1)]
polynomial = ''
number_roots = len(coefficients[::-1])
if number_roots < 1:
    polynomials = 'x = 0'
else:
    for i in range(number_roots):
        if i != number_roots - 1 and i != number_roots - 2 and coefficients[i] != 0:
            polynomial += f'{coefficients[i]}x^{number_roots - i - 1} '
            if coefficients[i + 1] != 0:
                polynomial += '+ '
        elif coefficients[i] != 0 and i == number_roots - 2:
            polynomial += f'{coefficients[i]}x '
            if coefficients[i + 1] != 0:
                polynomial += '+ '
        elif coefficients[i] != 0 and i == number_roots - 1:
            polynomial += f'{coefficients[i]} = 0'
        elif coefficients[i] == 0 and i == number_roots - 1:
            polynomial += '= 0'

with open('polynomials.txt', 'w') as data:
    data.write(polynomial)
