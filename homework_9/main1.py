'''
Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
'''

# import pygame as pg
# import sys
# from random import randint
#
# def check_win(array, symbol):
#     emty = 0
#     for row in array:
#         emty += row.count(0)
#         if row.count(symbol) == 3:
#             return f'Win {symbol}!'
#     for col in range(3):
#         if array[0][col] == symbol and array[1][col] == symbol and array[2][col] == symbol:
#             return f'Win {symbol}!'
#     if array[0][0] == symbol and array[1][1] == symbol and array[2][2] == symbol:
#         return f'Win {symbol}!'
#     if array[0][2] == symbol and array[1][1] == symbol and array[2][0] == symbol:
#         return f'Win {symbol}!'
#     if emty == 0:
#         return 'Draw!'
#     return False
# pg.init()
#
# screen_size = (300, 300)
# screen = pg.display.set_mode((screen_size))
# pg.display.set_caption('Крестики - нолики')
# red = (255, 0, 0)
# green = (0, 255, 0)
# white = (255, 255, 255)
# black = (0, 0, 0)
# margin = 10
# size_block = 87
# array = [[0 for _ in range(3)] for _ in range(3)]
# counter = 0
# game_over = False
# while True:
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             sys.exit(0)
#         elif event.type == pg.MOUSEBUTTONDOWN and not game_over:
#             x_mouse, y_mouse = pg.mouse.get_pos()
#             column = x_mouse // (margin + size_block)
#             row = y_mouse // (margin + size_block)
#             if array[row][column] == 0:
#                 array[row][column] = 'x'
#                 counter += 1
#         elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
#             game_over = False
#             array = [[0 for _ in range(3)] for _ in range(3)]
#             counter = 0
#             screen.fill(black)
#         game_over = check_win(array, 'x')
#         if game_over:
#             break
#
#         while counter % 2 and counter != 9:
#             bot_r = randint(0, 2)
#             bot_c = randint(0, 2)
#             if array[bot_r][bot_c] == 0:
#                 array[bot_r][bot_c] = 'o'
#                 counter += 1
#     if not game_over:
#         for row in range(3):
#             for col in range(3):
#                 if array[row][col] == 'x':
#                     color = red
#                 elif array[row][col] == 'o':
#                     color = green
#                 else:
#                     color = white
#                 x = col * size_block + (col + 1) * margin
#                 y = row * size_block + (row + 1) * margin
#                 pg.draw.rect(screen, color, (x, y, size_block, size_block))
#                 if color == red:
#                     pg.draw.line(screen, white, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 5)
#                     pg.draw.line(screen, white, (x + 5, y + size_block - 5), (x + size_block - 5, y + 5), 5)
#                 elif color == green:
#                     pg.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2-3, 5)
#
#     if (counter - 1) % 2:
#         game_over = check_win(array, 'o')
#     if game_over:
#         screen.fill(black)
#         font = pg.font.SysFont('stxingkai', 80)
#         text_1 = font.render(game_over, True, white)
#         text_rect = text_1.get_rect()
#         text_x = screen.get_width() / 2 - text_rect.width / 2
#         text_y = screen.get_height() / 2 - text_rect.height / 2
#         screen.blit(text_1, [text_x, text_y])
#     pg.display.update()

'''
 Напишите функцию to_dict(lst), которая принимает аргумент в виде списка 
 и возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
 Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
'''

# array = ['Москва', 'Брянск', 'Воронеж', 'Пенза']
# def to_dict(lst):
#     my_dict = {}
#     for item in lst:
#         my_dict[item] = item
#     return my_dict
# print(to_dict(array))

'''
Иван решил создать самый большой словарь в мире. Для этого он придумал функцию 
biggest_dict(**kwargs), которая принимает неограниченное количество параметров 
«ключ: значение» и обновляет созданный им словарь my_dict, состоящий всего из одного 
элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.
'''

# my_dict = {
#     'first_one': 'we can do it'
# }
# new_dict = {
#     'Car': 'BMW',
#     'Bike': 'Suzuki',
#     'Name': 'Mike'
# }
# def biggest_dict(input_dict, **kwargs):
#     for key, value in kwargs.items():
#         input_dict[key] = value
#     return input_dict
# my_dict = biggest_dict(my_dict, Москва=495, One=1)
# print(biggest_dict(my_dict, **new_dict))

'''
Дана строка в виде случайной последовательности чисел от 0 до 9.

Требуется создать словарь, который в качестве ключей будет принимать данные числа 
(т. е. ключи будут типом int), а в качестве значений – количество этих чисел в 
имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), 
принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.
'''

string = '4 6 5 6 4 28 87 23 98 45 78 78 6 3 5 58 65 78 98 98 4 4 5 5 5 6 6'
def count_it(sequence):
    numbers = [int(i) for i in sequence.split()]
    tmp_dict = dict()
    for item in numbers:
        count = 1
        for i in range(numbers.index(item) + 1, len(numbers)):
            if item == numbers[i]:
                count += 1
        tmp_dict[item] = count
    new_dict = dict()
    for _ in range(3):
        max_value = max(tmp_dict.values())
        for k, v in tmp_dict.items():
            if v == max_value:
                new_dict[k] = max_value
                tmp_dict.pop(k)
                break
    return new_dict

print(count_it(string))
