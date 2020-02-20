# 1.  Написати функцію, яка знаходить середнє арифметичне значення довільної кількості чисел.

def arifm(*args):
    return sum(args)/len(args)

lst = [int(input('a = ')) for _ in range(int(input('n = ')))]
print('SUM OF POS: {}'.format(sum(x for x in lst if x > 0)/len([x for x in lst if x > 0])))

# 2.  Написати функцію, яка повертає абсолютне значення числа
#
def new(a):
    return abs(a)

def my_abs(value):
    """Returns absolute value without using abs function"""
    if value <= 0:
        return value * -1
    return value * 1

# 3.  Написати функцію, яка знаходить максимальне число з двох чисел,
# а також в функції використати рядки документації DocStrings.

def max_int(a,b):
    ''' this func find max int'''
    return max(a,b)

print(max_int(2,4))
print(max_int.__doc__)


# 4.  Написати програму, яка обчислює площу прямокутника, трикутника та кола
# (написати три функції для обчислення площі, і викликати їх в головній програмі в залежності від вибору користувача)

def plosha():
    general = input('Зробіть вибір:\n1 - площа квадрату;\n'
                    '2 - площа трикутника; \n'
                    '3 - площа кола : ')
    if general == '1':
        return rectangle()
    elif general == '2':
        return triangle()
    elif general == '3':
        return circle()
#
#
def rectangle():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    return "Square={}".format(a * b)


def triangle():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    return "Area={}".format(0.5 * a * h)


def circle():
    PI = 3.14
    r = float(input("Input radius: "))
    return "Square={}".format(PI * r ** 2)


print(plosha())


# 5.  Написати функцію, яка обчислює суму цифр введеного числа.

def new_func(*args):
    return sum(*args)

def new_func_2(*args):
    product = 0
    for x in args:
        product += int(x)
    return product

print(new_func_2(2,6,7))

# 6.  Написати програму калькулятор, яка складається з наступних функцій:
# головної, яка пропонує вибрати дію та додаткових,
# які реалізовують вибрані дії, калькулятор працює доти, поки ми не виберемо дію вийти з калькулятора,
# після виходу, користувач отримує повідомлення з подякою за вибір нашого програмного продукту!!!

def general():
    text = input('Введіть операцію:\n'
                 '1 - додавання\n'
                 '2 - віднімання\n'
                 '3 - множення\n'
                 '4 - ділення\n'
                 '5 - вихід\n'
                 )
    while text == '1' or '2' or '3' or '4':
        if text == '1':
            return addition()
        elif text == '2':
            pass
        elif text == '3':
            return multiplication()
        elif text == '4':
            return division()
        elif text == '5':
            print('Дякую, що скористалися цим продуктом')
            exit()
        else:
            print('Введіть число від 1-5 для операції!\n')
            general()

def my_exit():
    text = input('Бажаєте продовжити операцію :\n'
          '1 - Так\n'
          '2 - Повернутися в головне меню\n')
    while text == '1' or '2':
        if text == '1':
            return __name__()
        else:
            return general()

def addition(*args):
    result = 0
    for args in input('Введіть числа для додавання: ').split():
        num = int(args)
        result += num
    print(f'Сумма чисел: {result}')
    text = input('Бажаєте продовжити операцію :\n'
          '1 - Так\n'
          '2 - Повернутися в головне меню\n')
    # while text == '1' or '2':
    #     if text == '1':
    #         return addition()
    #     else:
    #         return general()


def multiplication(*args):
    result = 1
    for args in input('Введіть числа для множення: ').split():
        num = int(args)
        result *= num
    print(f'Добуток чисел:{result}')
    text = input('Бажаєте продовжити операцію :\n'
          '1 - Так\n'
          '2 - Повернутися в головне меню\n')
    while text == '1' or '2':
        if text == '1':
            return __name__()
        else:
            return general()


def division(*args):
    new = []
    for args in input('Введіть числа для ділення: ').split():
        num = float(args)
        new.append(num)
    new_num = 0
    for _ in new:
        if new_num != [1]:
            new_num = new[0] / new[1]
            del new[:2]
            new.append(new_num)
            new = new[::-1]
    print(f'Частка чисел:{new[0]}\n')
    text = input('Бажаєте продовжити операцію :\n'
          '1 - Так\n'
          '2 - Повернутися в головне меню\n')
    while text == '1' or '2':
        if text == '1':
            return __name__()
        else:
            return general()


def subtraction(*args):
    new = []
    for args in input('Введіть числа для віднімання: ').split():
        num = float(args)
        new.append(num)
    new_num = 0
    for _ in new:
        if new_num != [1]:
            new_num = new[0] - new[1]
            del new[:2]
            new.append(new_num)
            new = new[::-1]
    print(f'Різниця чисел:{new[0]}')
    text = input('Бажаєте продовжити операцію?\n'
          '1 - Так\n'
          '2 - Повернутися в головне меню\n')
    while text == '1' or '2':
        if text == '1':
            return subtraction()
        elif text == '2':
            return general()

general()


# 7.1  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем.

def my_fibonacci(n):
    if n in (1,2):
        return 1
    return my_fibonacci(n-1) + my_fibonacci(n-2)

print(my_fibonacci(8))

# 7.2  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем, з допомогою
#lambda func

fib_2 = lambda n: fib_2(n - 1) + fib_2(n - 2) if n > 2 else 1
print(fib_2(8))

# 7.3  Побудувати рекурсивну функцію обчислення чисел Фібоначі до числа введеного користувачем, з допомогою
#функції, тут задійна швидкодія, так як ми запам'ятовуємо числав і не перебираємо
new_dict = {0: 0, 1: 1}

def fib_3(x):
    if x in new_dict:
        return new_dict[x]
    new_dict[x] = fib_3(x - 1) + fib_3(x - 2)
    return new_dict[x]

#8.  Написати програму, яка обчислює дискримінант квадратного рівняння

def discrim():
    a = float(input('Enter a :'))
    b = float(input('Enter b :'))
    c = float(input('Enter c :'))
    print(f'Discriminant is {b**2 - 4*a*c}')

discrim()




