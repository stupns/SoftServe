# Your collegue wrote an simple loop to list his favourite animals. But there seems to be a minor mistake in the
# grammar, which prevents the program to work. Fix it! :)


def list_animals(animals):
    print(len(animals))
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list


animals = ['dog', 'cat', 'elephant']

if __name__ == '__main__':
    assert list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'
    print('Well job!')
