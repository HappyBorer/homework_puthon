from data_output import cleaner_print
from reading_file import input_read
from adding_file import add_data
from data_search import pull_line
from sort_data import data_sort

keys = ['Last name', 'Name', 'Numbers', 'City']

def cart():
    global keys
    while True:
        print('Operations:')
        print('1.Reading an introductory file')
        print('2.Add data to the file')
        print('3.Search by request data')
        print('4.Sort data')
        print('5.Exit')
        enter = int(input('Select the operation: '))
        if not (0 < enter < 6):
            print('There is no such item in the menu. Repeat the input.')
            continue
        elif enter == 1:
            cleaner_print(input_read(input('Enter the CSV path for reading:')))
        elif enter == 2:
            print('Select the method of adding data')
            print('1.Adding data from CSV file')
            print('2.Adding data from the console')
            choice = int(input())
            if not (0 < choice < 3):
                print('Such a item is absent!')
                continue
            elif choice == 1:
                add_data(
                    input_read(input('The path of the CSV file from which data will be added: ')),
                    input('The path of the CSV file to which data will be added: '))
            elif choice == 2:
                n_data = []
                new_data = {}
                new_data[keys[0]] = (input('Last name: '))
                new_data[keys[1]] = (input('Name: '))
                new_data[keys[2]] = (int(input('Numbers: ')))
                new_data[keys[3]] = input('City: ')
                n_data.append(new_data)
                add_data(n_data, input('The path of the CSV file to which data will be added: '))
            print('Added!')
        elif enter == 3:
            print('Select the key to search')
            print('1.Last name')
            print('2.Name')
            print('3.Numbers')
            print('4.City')
            key = -1
            choice = int(input('Select: '))
            if not(0 < choice < 5):
                print('Such a item is absent!')
                continue
            elif choice == 1:
                key = 'Last name'
            elif choice == 2:
                key = 'Name'
            elif choice == 3:
                key = 'Numbers'
            else:
                key = 'City'
            cleaner_print(pull_line(key, input('Enter value: '), input('Enter the path to the CSV file: ')))
        elif enter == 4:
            print('Select the key to search')
            print('1.Last name')
            print('2.Name')
            print('3.Numbers')
            print('4.City')
            key = -1
            choice = int(input('Select: '))
            if not (0 < choice < 5):
                print('Such a item is absent!')
                continue
            elif choice == 1:
                key = 'Last name'
            elif choice == 2:
                key = 'Name'
            elif choice == 3:
                key = 'Numbers'
            else:
                key = 'City'
            print('1.Ascending')
            print('2.In descending')
            side = int(input('Select: ')) - 1
            if not(0 <= side < 2):
                print('Such a item is absent!')
                continue
            cleaner_print(data_sort(input_read(input('Enter the path to the CSV file: ')), key, side))
        else:
            choice = input('Exit(Y/N): ')
            if choice.upper() == 'Y':
                return
            else:
                continue

