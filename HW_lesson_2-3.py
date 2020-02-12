# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
def func_three():
    a = input('enter a: ')
    b = input('enter b: ')
    a, b = b, a
    print('a :{}, b :{}'.format(a, b))


func_three()


# 3 функція через тест
def func_three_assert(a: int, b: int):
    a, b = b, a
    return 'a :{}, b :{}'.format(a, b)


if __name__ == '__main__':
    assert func_three_assert(2, 4) == 'a :4, b :2'
    print('Well job, test 3 function is correct')
