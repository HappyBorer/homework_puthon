'''
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
    *Пример:*
    2+2 => 4;
    1+2*3 => 7;
    1-2*3 => -5;
- Добавьте возможность использования скобок, меняющих приоритет операций.
        *Пример:*
        1+2*3 => 7;
        (1+2)*3 => 9;
        9*(0+(4-2.5)/(3-2));
'''
def replacing_operations(op, total, exmp):
    exmp.pop(exmp.index(op) - 1)
    exmp.pop(exmp.index(op) + 1)
    exmp[exmp.index(op)] = total
    return exmp
def operations(expr):
    if '*' in expr:
        if '/' in expr:
            if expr.index('/') < expr.index('*'):
                total = expr[expr.index('/') - 1] / expr[expr.index('/') + 1]
                expr = replacing_operations('/', total, expr)
        else:
            total = expr[expr.index('*') - 1] * expr[expr.index('*') + 1]
            expr = replacing_operations('*', total, expr)
    elif '/' in expr:
        total = expr[expr.index('/') - 1] / expr[expr.index('/') + 1]
        expr = replacing_operations('/', total, expr)
    elif '+' in expr:
        if '-' in expr:
            if expr.index('-') < expr.index('+'):
                total = expr[expr.index('-') - 1] - expr[expr.index('-') + 1]
                expr = replacing_operations('-', total, expr)
        else:
            total = expr[expr.index('+') - 1] + expr[expr.index('+') + 1]
            expr = replacing_operations('+', total, expr)
    elif '-' in expr:
        total = expr[expr.index('-') - 1] - expr[expr.index('-') + 1]
        expr = replacing_operations('-', total, expr)
    return expr
def first_open(expa):
    first_op = len(expa)
    for i in range(first_op - 1, -1, -1):
        if expa[i] == '(':
            first_op = i
            break
    return first_op
def first_close(expa, first_op):
    first_cl = len(expa)
    for i in range(first_op, first_cl):
        if expa[i] == ')':
            first_cl = i
            break
    return first_cl

# import re
# string = input('Enter an example: ')
# exp = re.findall(r'\d+\.?\d+?|[\*\-\/\+]?|\d+|\(?\)?', string)
# exp = [i for i in exp if i not in '']
# for i in range(len(exp)):
#     if '.' in exp[i]:
#         exp[i] = float(exp[i])
#     elif exp[i].isdigit():
#         exp[i] = int(exp[i])
# while len(exp) > 1:
#     if '(' in exp:
#         prior = []
#         for i in range(first_open(exp) + 1, first_close(exp, first_open(exp))):
#             prior.append(exp[i])
#         for i in range(len(prior)):
#             for j in range(first_open(exp) + 1, first_close(exp, first_open(exp))):
#                 if exp[j] == prior[i]:
#                     exp.pop(j)
#         while len(prior) > 1:
#             prior = operations(prior)
#
#         exp.pop(first_close(exp, first_open(exp)))
#         exp[first_open(exp)] = prior[0]
#     else:
#         exp = operations(exp)
#
# print(exp[0])

'''
Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
Пример:
[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''
input_data = input('Enter the elements through a comma: ').split(', ')
unique_numbers = []
for i in range(len(input_data)):
    flag = True
    for j in range(len(input_data)):
        if i !=j and input_data[i] == input_data[j]:
            flag = False
            break
    if flag:
        unique_numbers.append(input_data[i])
print(unique_numbers)

'''
Задача FOOTBALL: (необязательное) Напишите программу, которая принимает на стандартный вход 
список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу 
результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:
Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
Прилагать скрины успешного запуска кода, в комментариях - ссылку на свой репозиторий в гитхабе с решением.
'''
