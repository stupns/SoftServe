# Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing.
# String should be capitalized and properly spaced. Using re and string is not allowed.


def filter_words(st):
    a = st.lower()
    b = a.upper()[0] + a[1:]
    c = b.split()
    return " ".join(c)


if __name__ == '__main__':
    assert filter_words('HELLO world!') == 'Hello world!'
    print("Well job!")