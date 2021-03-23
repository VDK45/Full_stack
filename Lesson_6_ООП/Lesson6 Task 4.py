"""
    4. Реализуйте базовый класс Car. 
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
    А также методы: go, stop, turn(direction), которые должны сообщать, 
    что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: 
    TownCar, SportCar, WorkCar, PoliceCar. 
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
    Для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
    должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов. 
    Выполните доступ к атрибутам, выведите результат. 
    Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.spe = speed
        self.col = color
        self.nam = name
        self.pol = is_police
        
    def star(self):
        return print(f"Car {self.col} {self.nam} starting")

    def stop(self):
        return print(f"Car {self.col} {self.nam} stoped")
        
    def turn(self, lr):
        if lr == "left":
            return print(f"Car {self.col} {self.nam} turn left ")
        elif lr == "right":         
            return print(f"Car {self.col} {self.nam} turn right ")
        else:
            return print(f"Car {self.col} {self.nam} not turn ")
    def show_speed(self):
        return print(f'{self.nam} едет со скоростью {self.spe}')
            
class TownCar(Car):
    
    def show_speed(self, speed_now):
            if speed_now <= 200:
                return super().show_speed() #show_speed из родителя
            if speed_now > 200:
                return print(f"Danger {self.nam} go with {speed_now} km/h Slow down")
            
class WorkCar(Car):
    
    def show_speed(self, speed_now):
            return print(f"Danger {self.nam} go with {speed_now} km/h Slow down") \
                   if speed_now > 200 else super().show_speed() #show_speed из родителя
                                          
class SportCar(Car):
    
    def show_speed(self):
        return print(f"{self.nam} with {self.spe}")

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name)
    
    def show_speed(self):
        return print(f"{self.nam} with {self.spe} km/h")


a = Car(200, "Red", "Toyota")
a.star()
a.stop()
a.turn("right")
b = TownCar(150, "black", "Lexus")
b.show_speed(150)
c = WorkCar(100, "Green", "Kamaz")
c.show_speed(280)
d = SportCar(300, "White", "Mustang")
d.show_speed()
d.turn("180")
p = PoliceCar(250, "white", "Police 911")
p.show_speed()
p.turn("left")
