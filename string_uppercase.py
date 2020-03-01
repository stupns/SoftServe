def is_uppercase(inp):
    if inp.isupper() == True:
        return True
    else:
        return False


if __name__ == '__main__':
    assert is_uppercase("c") == False
    assert is_uppercase("C") == True
    assert is_uppercase("hello I AM DONALD") == False
    assert is_uppercase("HELLO I AM DONALD") == True
    print("Well job!")
