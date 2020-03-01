# Write a program that finds the summation of every number from 1 to num. The number will always be a positive
# integer greater than 0.


def summation(num):
    return sum([x for x in range(1, num + 1)])


if __name__ == '__main__':
    assert summation(1) == 1
    assert summation(8) == 36
    assert summation(22) == 253
    assert summation(100) == 5050
    assert summation(213) == 22791
    print('Good job!')
