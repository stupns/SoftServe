# 1. Написати скрипт, який з двох введених чисел визначить, яке з них більше,
# а яке менше.
def int_is_bigg_or_small(a: int, b: int):
    return f'{a} is bigger than {b}' if a > b else f'{a} is smaller than {b}'


if __name__ == '__main__':
    assert int_is_bigg_or_small(2, 4) == '2 is smaller than 4'
    assert int_is_bigg_or_small(12, 5) == '12 is bigger than 5'
    print('Tests is passed')
#
# # 2. Написати скрипт, який перевірить чи введене число парне чи непарне
# # і вивести відповідне повідомлення.

def pair_or_no(text):
    text = int(input('enter int: '))
    return f'{text} is pair' if text % 2 == 0 else f'{text} is not pair'

if __name__ == '__main__':
    assert pair_or_no(2) == '2 is pair'
    assert pair_or_no(3) == '3 is not pair'
    print('Tests is passed')

# 3. Написати скрипт, який обчислить факторіал введеного числа.

number = int(input('enter int:'))
a = int(number)

while a !=1:
    number *=a-1
    a -=1
print(number)

# 3.1 Написати скрипт, який обчислить факторіал введеного числа.

chyslo = input('enter factorial :')
t = 1
for i in range(1, int(chyslo)+1):
    t *= i
print(t)

# 1. Роздрукувати всі парні числа менші 100  використовуючи цикл while

a = 1

while a < 100:
    if a % 2 == 0:
        print(a)
    a = a + 1

# 1.1 Роздрукувати всі парні числа менші 100 з використанням циклу for
for i in range(0,101,2):
   print(i)

# 2. Роздрукувати всі непарні числа менші 100. (написати два варіанти коду:
# один використовуючи оператор continue, а інший без цього оператора).

a = 0
while a < 100:
    a +=1
    if a % 2 == 0:
        continue
    else:
        print(a)

# 2.1 without continue

for i in range(1,100,2):
    print(i)

# 3. Перевірити чи список містить непарні числа.

spusok = [12,3,12,3,4]
only_odd =[num for num in spusok if num %2 == 0]
print(only_odd)

# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
num = 0


while num < len(list1):
    if num % 2 != 0:
       print(list1[num], end = " ")
    num += 1

# 4.  Створити список, який містить елементи цілочисельного типу, потім за
# допомогою циклу перебору змінити тип даних елементів на числа з плаваючою
# крапкою. (Підказка: використати вбудовану функцію float ()).


list2 = list(range(0,20))
for x in list2:
    list2[x] = float(list2[x])
print(list2)

# 5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи
#  цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)

number = int(input("Enter the int for generated sequence of Fibonacci:"))
fibo = [0, 1]
for i in range(number-1):
    fibo[i+1] = fibo[i-1] + fibo[i]
    fibo.append(fibo[i+1])
fibo.remove(fibo[i+1])
print(fibo)

# 6.  Створити список, що складається з чотирьох елементів типу string. Потім,
#  за допомогою циклу for, вивести елементи по черзі на екран.

spysok = ["Hello,", "World!", "Whats", "up?"]
for i in spysok:
    print(i)

# 7.  Знайти прості числа від 10 до 30, а всі решта чисел представити у вигляді добутку чисел
# (наприклад 10 equals 2 * 5
#                     11 is a prime number
#                     12 equals 2 * 6
#                     13 is a prime number
#                     14 equals 2 * 7
#                      ………………….)

new_list = list(range(0, 50))
#
for i in new_list:
    if 10 <= i <= 30:
        if i % 2 == 0:
            print(f'{i} equals 2 * {i // 2}')
        else:
            print(f'{i} is a prime number')
    else:
        print(f'{i} it number goes beyond')

# 5.  Перший випадок.
# Написати програму, яка буде зчитувати числа поки не зустріне від’ємне число.
# При появі від’ємного числа програма зупиняється (якщо зустрічається 0 програма теж зупиняється).

create_list = [1,23,43,-2,22,2,-43]

for i in create_list:
    if i <= 0:
        break
    else:
        print(i)

# 4.  Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)

login = input('Enter login:')
while login != 'First':
    print('Login is failed')
    break
else:
    print('Hello, user')
