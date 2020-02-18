# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


if __name__ == '__main__':
    assert create_array(1) == [1]
    assert create_array(2) == [1, 2]
    assert create_array(3) == [1, 2, 3]
    assert create_array(4) == [1, 2, 3, 4]
    assert create_array(5) == [1, 2, 3, 4, 5]
    print("Well job!")
