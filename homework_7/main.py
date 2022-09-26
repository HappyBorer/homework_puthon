'''
Разделим сервис на этапы:
Как можно вводить данные?
‘Фамилия Имя Номер’
Как их обрабатывать? Где хранить?
user = {‘Name’:’’, ‘Last Name’:’’, ‘number’:’’ }
user_list = [user1,user2,user3……]
Как запрашивать и получать данные?
Какие функции можно для этого создать?
Как вынести функции в модули?
'''
keys = ['Last name', 'Name', 'Numbers']

def input_read(path):
    try:
        file = open(path, 'r', encoding='utf8')
        temp = file.read().split('\n')
        file.close()
    except:
        print('Not file')
        exit()
    lines = []
    for elem in temp:
        temp_dict = {}
        person = elem.split(';')
        for i in range(len(person)):
            temp_dict[keys[i]] = person[i]
        lines.append(temp_dict)
    return lines

def add_data(data, path = 'data.csv'):
    file = open(path, 'a', encoding='utf8')
    for line in only_new(data):
        temp = ''
        for element in line:
            temp += str(line[element]) + ';'
        file.write(temp[:-1] + '\n')
    file.close()

def only_new(data, path = 'data.csv'):
    already_exists = input_read(path)
    return [element for element in data if element not in already_exists]

def pull_line(key, value, path = 'data.csv'):
    data = input_read(path)
    print(data)
    return [line for line in data if line[key] == value]

#add_data(input_read('input_data.csv'))
print(pull_line('Name', 'Семен'))


