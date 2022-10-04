import csv
import menu
def input_read(path):
    try:
        with open(path, 'r', newline='', encoding='cp1251') as file:
            temp = csv.DictReader(file)
            lines = []
            for elem in temp:
                temp_dict = {}
                for i in range(len(elem)):
                    temp_dict[menu.keys[i]] = elem[menu.keys[i]]
                lines.append(temp_dict)
        file.close()
        return lines
    except:
        return 'Not file'
