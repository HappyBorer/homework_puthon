"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
"""
number = input('Введите вещественное число:\n')
digits = 1
if '.' in number:
    digits = 10 ** len(number.split('.')[1])
number = float(number) * digits
total = 0
while number > 0:
    total += int(number % 10)
    number = number // 10
print(f'Сумма всех цифр вещественного числа равна {total}')
