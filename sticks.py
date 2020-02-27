# In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. The last person to
# take a stick wins.


def make_move(sticks):
    return sticks % 4


if __name__ == '__main__':
    assert make_move(3) == 3
    print("Well job!")