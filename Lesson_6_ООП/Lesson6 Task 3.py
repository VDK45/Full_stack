"""
    3. Реализовать базовый класс Worker (работник), 
    в котором определить атрибуты: name, surname, position (должность), income (доход). 
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
    оклад и премия, например, {"wage": wage, "bonus": bonus}. 
    Создать класс Position (должность) на базе класса Worker. 
    В классе Position реализовать методы получения полного имени сотрудника 
    (get_full_name) и дохода с учетом премии (get_total_income). 
    Проверить работу примера на реальных данных (создать экземпляры класса Position, 
    передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    def __init__(self, name, surname, position, income={"wage": 20000, "bonus": 5000}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        
class Position(Worker):
    
    def get_full_name(self):
        return print(f"Full name: {self.surname} {self.name}")
        
        
    def get_total_income(self):
        return print(sum(self._income.values()))
        
a = Position("Иванов", "Иван", "Director")        

a.get_full_name()
a.get_total_income()
b = Worker("VDK", "45", "Player")

print('-------------- Вариант ------------')

class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        print('Добавлен  сотрудник: ')


class Position(Worker):
    def get_full_name(self):
        return print(f"{self.position}:  {self.name} {self.surname}")

    def get_total_income(self):
        total = sum(self._income.values())
        return print(f"{self.name} {self.surname} получает {total} рублей")


person_1 = Position('Евгений', 'Колмаков', 'Директор', 600000, 567899)
person_1.get_full_name()
person_1.get_total_income()

person_2 = Position('Иван', 'Иванов', 'Менежер', 300000, 45899)
person_2.get_full_name()
person_2.get_total_income()

