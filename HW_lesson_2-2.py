# Задано чотирицифрове натуральне число.
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число


def func_two():
    n = input('input four integers: ')
    summ = 1
    for i in n:
        summ *= int(i)
    print(' product of all mumeric values : {},\n reversed of all mumeric values : {},'
          '\n sorted of all mumeric values :  {}'.format(summ, n[::-1], ''.join(sorted(n))))


func_two()


# 2 функція через тест
def func_two_assert(a: str):
    summ = 1
    for i in a:
        summ *= int(i)
    return '{}, {}, {}'.format(summ, a[::-1], ''.join(sorted(a)))


if __name__ == '__main__':
    new_list = [72, 3423, 2334]
    assert func_two_assert('3243') == '72, 3423, 2334'
    print('Well job, test 2 function is correct')