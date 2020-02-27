# In this kata you will create a function that takes in a list and returns a list with the reverse order.


def reverse_list(l):
    return l[::-1]


if __name__ == '__main__':
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_list([3, 1, 5, 4]) == [4, 5, 1, 3]
    print("Well job!")
