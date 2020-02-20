import pyowm
import random
from math import pi, pow
import timeit

owm = pyowm.OWM('7ea08a61ea3e979d8f0d7c5842fc8b4f')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
place = input('Enter you city name:')
observation = owm.weather_at_place(place)
w = observation.get_weather()  # status=Clouds>

# Weather details
w.get_wind()  # {'speed': 4.6, 'deg': 330}
w.get_humidity()  # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print(f"speed:{w.get_wind()['speed']}, deg:{w.get_wind()['deg']} ")
print("Himidility", w.get_humidity())
print(f"temp_max: {w.get_temperature('celsius')['temp_max']}, temp:"
      f"{w.get_temperature('celsius')['temp']}, temp_min:{w.get_temperature('celsius')['temp_min']}")

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)

# TASK 2

a = random.randint(1, 100)
user = int(input('Input some number:'))
print(a)
while a != user:
    if a < user:
        user = int(input('Your number is smallest than machine int: '))
    elif user < a:
        user = int(input('Your number is biggest than machine int: '))

print('You best')


# 2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2.
# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі).
#
def kvadrat():
    a = int(input('enter a:'))
    b = int(input('enter a:'))
    return f'{pow(a * b, 2)}'


def trik():
    a = int(input('enter a:'))
    h = int(input('enter h:'))
    return f'{pow(0.5*a*h, 2)}'


def circle():
    r = int(input('enter r:'))
    return f'Plosha circle :{pi * pow(r, 2)}'


print(circle())
