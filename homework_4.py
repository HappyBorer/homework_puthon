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
'''
Задайте последовательность чисел. Напишите программу, которая 
выведет список неповторяющихся элементов исходной последовательности.
'''
numbers = input('Enter the numbers through the gap: ')
some_list = set()
numbers_list = numbers.split(' ')
for i in range(len(numbers_list)):
    some_list.add(int(numbers_list[i]))
print(some_list)
