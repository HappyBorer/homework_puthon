import os
import csv
from reading_file import input_read
import menu

def add_data(data, path='data.csv'):
    if os.stat(path).st_size == 0:
        with open(path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=menu.keys)
            writer.writeheader()
        file.close()
    else:
        with open(path, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=menu.keys)
            new_data = only_new(data, path)
            writer.writerows(new_data)
        file.close()
def only_new(data, path = 'data.csv'):
    already_exists = input_read(path)
    return [element for element in data if element not in already_exists]
