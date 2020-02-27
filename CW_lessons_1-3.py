def greet(name):
    return 'Hello, my love!' if name == "Johnny" else f'Hello, {name}!'


if __name__ == '__main__':
    assert greet('Johnny') == 'Hello, my love!'
    assert greet('Igor') == 'Hello, Igor!'
    print('Well job! Tests task is correct')