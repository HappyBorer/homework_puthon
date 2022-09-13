'''
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''

accuracy, number = float(input('Enter accuracy: ')), float(input('Enter number: '))
accuracy = len(str(accuracy).split('.')[1])
number = (number * 10 ** accuracy // 1) / 10 ** accuracy
print(f'{number:.{accuracy}f}')

'''

'''