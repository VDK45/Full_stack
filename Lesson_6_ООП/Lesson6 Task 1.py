"""
    1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: 
    красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, 
    второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
    Задачу можно усложнить, реализовав проверку порядка режимов, 
    и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import  time

class TrafficLight:
    def __init__(self, c):
        self.__color = c
        
    def running(self, g="Green", y="Yellow", r="Red"):
        while 1:
            if g != "Green" or y != "Yellow" or r != "Red":
                break
            print(g)
            time.sleep(3)
            print(y)
            time.sleep(1)
            print(r)
            time.sleep(3)
            print(y)
            time.sleep(1)
            if self.__color == "q":
                break
                
    def set_color(self, color):
        self.__color = color
        print(f"Set privat color {self.__color}")
            
    def get_color(self):
        print(f"Get pivate color: {self.__color}")
         
a = TrafficLight("GYR")
a.set_color("q")
a.get_color()
a.running("Green", "Yellow", "Red")

print("-------------- Вариант -----------------")
"""
    Корректно работает в Pycharm
"""
import itertools

class TrafficLight:
    __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            time.sleep(light[1][0])

trafficLight_1 = TrafficLight()
trafficLight_1.running()






