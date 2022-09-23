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

import re
string = input()
exp = re.findall(r'\d+\.?\d+?|[\*\-\/\+]?|\d+|\(?\)?', string)
exp = [i for i in exp if i not in '']
for i in range(len(exp)):
    if '.' in exp[i]:
        exp[i] = float(exp[i])
    elif exp[i].isdigit():
        exp[i] = int(exp[i])
while len(exp) > 1:
    if '(' in exp:
        prior = []
        for i in range(first_open(exp) + 1, first_close(exp, first_open(exp))):
            prior.append(exp[i])
        for i in range(len(prior)):
            for j in range(first_open(exp) + 1, first_close(exp, first_open(exp))):
                if exp[j] == prior[i]:
                    exp.pop(j)
        while len(prior) > 1:
            prior = operations(prior)

        exp.pop(first_close(exp, first_open(exp)))
        exp[first_open(exp)] = prior[0]
    else:
        exp = operations(exp)

print(exp[0])
