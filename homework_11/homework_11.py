class Person:
    def __init__(self, name, mid_name, surname, dict_ph):
        self.name = name
        self.mid_name = mid_name
        self.surname = surname
        self.dict_ph = dict_ph

    def get_phone(self):
        return self.dict_ph.get('private')

    def get_name(self):
        return f'{self.name} {self.mid_name} {self.surname}'

    def get_work_phone(self):
        return self.dict_ph.get('work')

    def get_sms_text(self):
        return f'Уважаемый {self.name} {self.mid_name}! ' \
               f'Примите участие в нашем безпроигрышном конкурсе для физических лиц'


class Company:
    def __init__(self, name_comp, type_comp, dict_ph_comp, *persone):
        self.name_comp = name_comp
        self.type_comp = type_comp
        self.dict_ph_comp = dict_ph_comp
        self.some_list = list(persone)

    def get_phone(self):
        if self.dict_ph_comp.get('contact'):
            return self.dict_ph_comp.get('contact')
        else:
            for i in range(len(self.some_list)):
                work_phone = self.some_list[i].get_work_phone()
                if work_phone != None:
                    return self.some_list[i].get_work_phone()
                elif i == (len(self.some_list) - 1):
                    return self.some_list[i].get_work_phone()

    def get_name(self):
        return self.name_comp

    def get_sms_text(self):
        return f'Для компании {self.name_comp} есть супер предложение! ' \
               f'Примите участие в нашем беcпроирышнем конкурсе для {self.type_comp}'


def send_sms(*obj):
    for i in obj:
        phone = i.get_phone()
        if phone != None:
            print(f'Отправлено СМС на номер {i.get_phone()} с текстом: {i.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {i.get_name()}')


# person1 = Person('Ivan', 'Ivanovich', 'Ivanov', {'private': 123, 'work': 456})
# person2 = Person('Ivan', 'Petrovich', 'Petrov', {'private': 789})
# person3 = Person('Ivan', 'Petrovich', 'Sidorov', {'work': 789})
# person4 = Person('John', 'Unknown', 'Doe', {})
# company1 = Company('Bell', 'OOO', {'contact': 111}, person3, person4)
# company2 = Company('Cell', 'AO', {'non_contact': 222}, person2, person3)
# company3 = Company('Dell', 'Ltd', {'non_contact': 333}, person2, person4)
# send_sms(person1, person2, person3, person4, company1, company2, company3)

class MinStart:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        try:
            return min(self.numbers)
        except:
            return None


class MaxStart:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        try:
            return max(self.numbers)
        except:
            return None


class AverageStart:
    def __init__(self):
        self.numbers = []

    def add_number(self, number):
        self.numbers.append(number)

    def result(self):
        try:
            return sum(self.numbers) / len(self.numbers)
        except:
            return None


values = [1, 2, 4, 5]

mins = MinStart()
maxs = MaxStart()
average = AverageStart()

for i in values:
    mins.add_number(i)
    maxs.add_number(i)
    average.add_number(i)

print(mins.result(), maxs.result(), average.result())
