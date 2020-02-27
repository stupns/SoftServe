# 1.  Створити клас машина з атрибутами name,  make, model та методами start та stop,
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.


class Car:
    def __init__(self, name, make, model):
        self.car_name = f'car name is {name}'
        self.car_make = f'from : {make}'
        self.car_model = f'model is a {model}'

    def start(self):
        print(f'Your {self.car_name}, {self.car_model} {self.car_make} is started ')

    def stop(self):
        print(f'Your {self.car_name}, {self.car_model} {self.car_make} is stopped')


a = Car('Shevrolette', 'China', 'Lachetti')
a.start()
a.stop()


# 2.  Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення “Hello,
# my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль, в якому конструктор встановлює
# ім’я, а метод move виводить повідомлення {ім’я конкретного екземпляра класу}  moves at the speed {speed(цей
# параметр метод move отримує як вхідний)} km / h


class Person:
    def __init__(self, name):
        self.person_name = name

    def info(self):
        print(f'Hello, my name is {self.person_name}')


class Car:
    def __init__(self, name):
        self.car_name = name

    def move(self, speed):
        print(f'Max speed {self.car_name} is {speed} km/h')


per_info = Person("Serhii")
per_info.info()

car_audi = Car("Chevrolette")
car_audi.move("320")
