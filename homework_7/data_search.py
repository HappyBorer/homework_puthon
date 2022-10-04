from reading_file import input_read
def pull_line(key, value, path = 'data.csv'):
    data = input_read(path)
    try:
        return [line for line in data if line[key] == value]
    except:
        return ['No key']
