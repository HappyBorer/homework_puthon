import menu

def cleaner_print(output):
    try:
        for dict in output:
            result = ''
            for i in range(len(dict)):
                result += f'{menu.keys[i]} : {dict[menu.keys[i]]}; '
            if output[-1] == dict:
                print(result[:-2])
            else:
                print(result[:-1])
    except:
        print(output)


