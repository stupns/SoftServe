

# try:
#     a = int(input('press int: '))
#     if a % 2 == 0 :
#         print(f'{a} it int is odd')
#     elif a % 2 != 0:
#         print(f'{a} is not even')
# except ValueError:
#     print('is type uncorrected, print pls integer')

# 2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є
# парним чи непарним числом. Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати
# власну виняткову ситуацію. Головний код має викликати функцію, яка обробляє введену інформацію.

# def enterage(age):
#     age = int(input('press age: '))
#     if age % 2 < 0:
#         print(f'{age} this age is odd')
#     else:
#         print(f'{age} this age is even')
#
#
# try:
#     age = int(input('Enter you age: '))
#     enterage(age)
#
# except ValueError:
#     print('Print only  positive integers')
# except:
#     print('something is wrong')

# 3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому,
# передбачити випадок ділення на нуль, випадки синтаксичних помилок та випадки інших виняткових ситуацій.
# Використати блоки else та finaly.

# try:
#     num1, num2 = eval(input("Enter two numbers, separated by a comma : "))
#     result = num1 / num2
#     print("Result is", result)
#
# except ZeroDivisionError:
#     print("Division by zero is error !!")
#
# except SyntaxError:
#     print("Comma is missing. Enter numbers separated by comma like this 1, 2")
# # 65866hgjh75785
# except:
#     print("Wrong input")
#
# else:
#     print("No exceptions")
#
# finally:
#     print("This will execute no matter what")

# 4. Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня,
# який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) .
# Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.


class OutOfDayIndex(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class NotNegativeDays(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


try:
    n = int(input("Input an integer between 1 and 7: "))
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if n in range(1, 8):
        print(f'Today is {days_of_week[n-1]}')
    if n > 7:
        raise OutOfDayIndex("There are only seven days!")
    if n < 1:
        raise NotNegativeDays("Day index cannot be negative or equal to zero!")

except OutOfDayIndex as e:
    print(e.data)
except NotNegativeDays as e:
    print(e.data)
except ValueError:
    print("Value Error")
finally:
    print("End of the program.")




