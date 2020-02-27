# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.


def bool_to_word(boolean):
    if boolean == 1:
        return 'Yes'
    elif boolean == 0:
        return 'No'


if __name__ == '__main__':
    assert bool_to_word(True) == 'Yes'
    assert bool_to_word(False) == 'No'
    print("Well job!")