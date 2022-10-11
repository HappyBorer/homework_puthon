'''
Создать класс TrafficLight (светофор):
- определить у него один атрибут color (цвет) и метод running (запуск);
- атрибут реализовать как приватный;
- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
- продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
- переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
- проверить работу примера, создав экземпляр и вызвав описанный метод.

'''
# import time
#
# class TrafficLight:
#     def __init__(self):
#         self.__color = ['Red', 'Yellow', 'Green']
#
#     def running(self):
#         print('Stop ctrl + f2')
#         try:
#             while True:
#                 print(self.__color[0])
#                 time.sleep(7)
#                 print(self.__color[1])
#                 time.sleep(2)
#                 print(self.__color[2])
#                 time.sleep(15)
#         except KeyboardInterrupt:
#             print('End')
#
# traffic = TrafficLight()
#
# traffic.running()

'''
Реализовать класс Road (дорога).
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
- использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
- проверить работу метода.
'''

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_asphalt(self, mass, thickness):
        return self._length * self._width * (mass / 1000) * thickness

road = Road(5000, 20)
print(road.mass_asphalt(25, 5))
