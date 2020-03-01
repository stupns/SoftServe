# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.


def double_char(s):
    new_s = ''
    for x in range(len(s)):
        new_s += s[x] * 2
    return new_s


if __name__ == '__main__':
    assert double_char("String") == "SSttrriinngg"
    assert double_char("Hello World") == "HHeelllloo  WWoorrlldd"
    assert double_char("1234!_") == "11223344!!__"
    print("Well job!")
