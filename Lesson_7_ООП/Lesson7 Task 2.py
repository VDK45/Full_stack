"""
    2. h
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
    Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани. 
    Проверить на практике полученные на этом уроке знания: 
    реализовать абстрактные классы для основных классов проекта, 
    проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod
from typing import Any


class Clothes(ABC):
    """Interface """
       
    
    @abstractmethod  
    def cal_costume(self):
        pass

    @abstractmethod  
    def cal_jacket(self):
        pass

class Costume(Clothes):
    def __init__(self, h):
        self.h = h
        
    @property
    def h(self):
        return self.__h
        
    @h.setter
    def  h(self, h):
        if h < 0:
            self.__h = 0
        elif h > 1000:
            self.__h = 1000
        else:
            self.__h = h
            
    def get_h(self):
        return print(f"self.h = {self.h}")
    
    def cal_costume(self):
        return 2 * self.h + 0.3
    def cal_jacket(self):
        pass
        
class Jacket(Clothes):
    def __init__(self, v):
        self.v = v
        
    @property
    def v(self):
        return self.__v
        
    @v.setter
    def v(self, v):
        if v < 0:
            self.__v = 0
        elif v > 1000:
            self.__v = 1000
        else:
            self.__v = v
            
    def get_v(self):
        return print(f"self.v = {self.v}") 
    
    def cal_jacket(self):
        return self.v / 6.5 + 0.5
    def cal_costume(self):
        pass  # @abstractmethod  
        
        
h1 = Costume(4000)
h1.get_h()
print(h1.cal_costume())
v1 = Jacket(4000)
v1.get_v()
print(v1.cal_jacket())

print('----------- Вариант учительский ------------')

class Clothes(ABC):
    result = 0

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        Clothes.result += self.consumption + other.consumption
        return Costume(0)

    def __str__(self):
        return f"{Clothes.result}"


class Coat(Clothes):
    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def consumption(self):
        return round((2 * self.param + 0.3) / 100)

coat = Coat(42)
costume = Costume(170)
print(coat + costume + coat)

print('----------- Вариант учительский 2 ----------')

class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet

class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Только с 40 размера')
            self.__size = 40
        elif size > 60:
            print('До 60 размера')
            self.__size = 60
        else:
            self.__size = size

    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('Только с 150 см ')
            self.__height = 150
        elif height > 240:
            print('До 240 см')
            self.__height = 240
        else:
            self.__height = height

    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3

coat_1 = Coat(int(input('Размер пальто: ')))
print(f'Потребуется {coat_1.raschet:.2f} метров ткани на пальто {coat_1.size} размера')
costume_1 = Costume(int(input('Рост костюма в см: ')))
print(f'Потребуется {costume_1.raschet:.2f} метров ткани на пальто {costume_1.height} роста')
print(f'Всего потребуется {coat_1 + costume_1:.2f} метров ткани')

            
