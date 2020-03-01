# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of
# order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

def sorter(textbooks):
    return sorted(textbooks, key=lambda e: e.lower())


if __name__ == '__main__':
    assert sorter(['Algebra', 'History', 'Geometry', 'English']) == ['Algebra', 'English', 'Geometry', 'History']
    assert sorter(['Algebra', 'history', 'Geometry', 'english']) == ['Algebra', 'english', 'Geometry', 'history']
    assert sorter(['Alg#bra', '$istory', 'Geom^try', '**english']) == ['$istory', '**english', 'Alg#bra', 'Geom^try']
    print("Well job!")
