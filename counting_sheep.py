# Consider an array of sheep where some sheep may be missing from their place.
# We need a function that counts the number of sheep present in the array (true means present).


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]


def count_sheeps(arrayOfSheeps):
    a = int(0)
    for x in (arrayOfSheeps):
        if x == 1:
            a += 1
    return a


if __name__ == '__main__':
    assert count_sheeps(array1) == 17
    print("Well job!")
