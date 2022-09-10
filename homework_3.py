"""
Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""
# small_list = [int(input('Enter the element: ')) for _ in range(int(input('Enter the number of element: ')))]
# sum_item = 0
# for i in range(len(small_list)):
#     if i % 2 == 1:
#         sum_item += small_list[i]
# print(f'Сумма элементов стоящих на нечётных позициях равна {sum_item}')

'''
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''


# list_numbers = [int(input('Enter the element: ')) for _ in range(int(input('Enter the number of element: ')))]

def work_of_steam(kit):
    work_steam = []
    for i in range(len(kit) // -2 * -1):
        work_steam.append(kit[i] * kit[(i + 1) * -1])
    return work_steam


# print(work_of_steam(list_numbers))

'''
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''


# list_numbers = [float(input('Enter the element: ')) for _ in range(int(input('Enter the number of element: ')))]

def difference_min_max_factional_part(some_list):
    new_list = []
    for i in some_list:
        sigans = len(str(i).split('.')[1])
        if i - int(i) != 0:
            new_list.append(round(i - int(i), sigans))
    return max(new_list) - min(new_list)


# print('The difference between the maximum and minimum fractional part of the element is equal', end=' ')
# print(difference_min_max_factional_part(list_numbers))

'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

# number = int(input('Enter a number: '))
# double_number = ''
# while number > 0:
#     double_number = str(number % 2) + double_number
#     number = number // 2
# print('In binary calculus', double_number)

'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
size = int(input('Enter the number: '))
fibonachi_digit = []


def fibonachi(number):
    if number in [1, 2]:
        return 1
    else:
        return fibonachi(number - 1) + fibonachi(number - 2)


for i in range(1, size + 1):
    fibonachi_digit.append(fibonachi(i))

neg_fibonachi = [0, 1]
for i in range(2, size + 1):
    neg_fibonachi.append(neg_fibonachi[i-2]-neg_fibonachi[i-1])
neg_fibonachi.reverse()
fibonachi_digit = neg_fibonachi + fibonachi_digit
print(fibonachi_digit)

