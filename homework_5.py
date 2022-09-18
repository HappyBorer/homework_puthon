'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''
# text = input().split(' ')
# result = (list(filter(lambda x: 'а' not in x, filter(lambda x: 'б' not in x,
#           filter(lambda x: 'в' not in x, text)))))
# print(' '.join(result))

'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
ход друг после друга. Первый ход определяется жеребьёвкой. За один ход 
можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''
# from random import randint
# candies = 2021
# step = 28
# i = randint(0, 1)
# human, bot, previous = 0, 0, candies
# current = candies
# menu = 0
# while True:
#     print('Choosing a game: \n1. Player 1 vs Player 2\n2. Player vs Bot(light)\n3. Player vs Bot(hard)')
#     menu = int(input('Select the game: '))
#     if 0 < menu < 4:
#         break
#     else:
#         print('Not the right choice! Repeat!')
#
# #  Играют два игрока
#
# if menu == 1:
#     players = ['first player', 'second player']
#     print(f'The first move {players[i]}')
#     while candies > 0:
#         player = int(input(f'Step {players[i]}: '))
#         if player > step or player == 0:
#             print('Not the right number of sweets! Enter again!')
#             continue
#         candies -= player
#         if candies == 0:
#             print(f'The {players[i]} won!')
#         print(f'The current amount of sweets {candies}')
#         if i == 0:
#             i = 1
#         else:
#             i = 0
#
# # Игра с ботом
# elif menu == 2:
#     if i != 0:
#         print('The first move human')
#     else:
#         print('The first move bot')
#     while candies > 0:
#         if i != 0:
#             human = int(input('The step of the person: '))
#             if human > step or human == 0:
#                 print('Not the right number of sweets! Enter again!')
#                 continue
#             candies -= human
#             if candies == 0:
#                 print('The human won!')
#         else:
#             bot = randint(1, 28)
#             if candies - bot < 0:
#                 continue
#             print(f'The step of the bot: {bot}')
#             candies -= bot
#             if candies == 0:
#                 print('The bot won!')
#         print(f'The current amount of sweets {candies}')
#         if i != 0:
#             i = 0
#         else:
#             i = 1
#
# # Бот с небольшим интеллектом
#
# else:
#     if i != 0:
#         print('The first move human')
#     else:
#         print('The first move bot')
#     while current > 0:
#         if i != 0:
#             human = int(input('The step of the person: '))
#             if human > step or human == 0:
#                 print('Not the right number of sweets! Enter again!')
#                 continue
#             current -= human
#             if current <= 0:
#                 print('The human won!')
#         else:
#             if current == candies:
#                 bot = 20
#             elif current > candies - 20:
#                 bot = current - (candies - 20)
#             elif current <= step:
#                 bot = current
#             elif current % (step + 1) != 0:
#                 bot = current % (step + 1)
#             else:
#                 bot = randint(1, 28)
#             print(f'The step of the bot: {bot}')
#             current -= bot
#             if current <= 0:
#                 print('The bot won!')
#             previous = current
#         print(f'The current amount of sweets {current}')
#         if i != 0:
#             i = 0
#         else:
#             i = 1

'''
Создайте программу для игры в ""Крестики-нолики"".
'''
def field():
    fld = [1, 2, 3]
    fld_1 = [4, 5, 6]
    fld_2 = [7, 8, 9]
    print(fld)
    print(fld_1)
    print(fld_2)


