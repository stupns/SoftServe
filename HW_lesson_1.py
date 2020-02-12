# Task1 Method one Define variables a and b. Read values a and b from console and calculate
def func_task1(a: int, b: int, operation: str) -> int:
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        return a // b

if __name__ == '__main__':
    assert func_task1(2, 4, '+') == 6
    assert func_task1(3, 5, '*') == 15
    print("Well job!")


# Task1 Method two Define variables a and b. Read values a and b from console and calculate
def func_task1_1():
    a = int(input('Input а: '))
    b = int(input('Input b: '))

    operation = '{}'.format(str(input('Input operation: ')))
    if operation == '*':
        print('{} {}'.format('Result a * b =', (a * b)))
    if operation == '+':
        print('{} {}'.format('Result a + b =', (a + b)))
    if operation == '-':
        print('{} {}'.format('Result a - b =', (a - b)))
    if operation == '/':
        print('{} {}'.format('Result a / b =', (a / b)))

func_task1_1()


# Task1 Method three Define variables a and b. Read values a and b from console and calculate

def func_task1_2():
    global a, b
    try:
        a = int(input('Input а: '))
    except ValueError:
        print('Input please integer value')
        func_task1_2()
    try:
        b = int(input('Input b: '))
    except ValueError:
        print('Input please integer value')
        func_task1_2()
    text = '{}'.format(str(input('Input operation: ')))
    addition = '+'
    subtraction = '-'
    division = '/'
    multiplication = '*'
    if text.count(addition) == 1:
        print(a + b)
        return a + b
    if text.count(multiplication) == 1:
        print(a * b)
        return a * b
    if text.count(subtraction) == 1:
        print(a - b)
        return a - b
    if text.count(division) == 1:
        print(a / b)
        return a / b
    else:
        print('Operation not found. Please enter correct declared operation ')
        return func_task1_2()

func_task1_2()

# enter answers to question

# Task2 Method One Output question “What is your name?“, “How old are you?“, Where do you live?“.
# Read the answer of user and output next information: “Hello, (answer(name))“, “Your age is  (answer(age))“,
# “You live in  (answer(city))“
def func_task2():
    name = input('What is your name?\n' + 'Name: ')
    if name == '':
        print('Your name can`t be empty. Plz input correct name.')
        return func_task2()
    age = input('How old are you?\n' + 'Age: ')
    if age == '':
        print('Your age can`t be empty. Plz input correct age.')
        return func_task2()
    live = input('Where do your live?\n' + 'City: ')
    if age == '':
        print('Your age can`t be empty. Plz input correct age.')
        return func_task2()
    result = ('Result:\n'
                  'Hello, {}!\n'
                  'Your age is {}.\n'
                  'You live in {}.'.format(name,age,live))
    print(result)

func_task2()

# Task2 Method Two

def func_task2_2(name: str, age: int, city: str) -> str:
    if name == '':
        return ('Your name can`t be empty. Plz input correct name.')
    if age == '':
        return ('Your age can`t be empty. Plz input correct age.')
    if city == '':
        return ('Your city can`t be empty. Plz input correct city.')
    result = ('Result:\n'
              'Hello, {}!\n'
              'Your age is {}.\n'
              'You live in {}.'.format(name, age, city))
    return result


if __name__ == '__main__':
    assert func_task2_2('serhii', 12, 'lviv') == ('Result:\n' + 'Hello, serhii!\n' + 'Your age is 12.\n' +
                                                'You live in lviv.')
    assert func_task2_2('', 12, 'lviv') == ('Your name can`t be empty. Plz input correct name.')
    print('Well job!')