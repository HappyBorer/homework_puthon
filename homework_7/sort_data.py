import menu
def data_sort(data, key, side):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            if side:
                if data[j][key] < data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if data[j][key] > data[j + 1][key]:
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data
