def reverse(st):
   st = st.split()
   st = st[::-1]
   st = ' '.join(st)
   return st

# 2 method
def reverse2(st):
   return ' '.join(st.split()[::-1])

# 3 method
def reverse3(st):
   return " ".join(reversed(st.split())).strip()

if __name__ == '__main__':
    assert reverse('Hi There.') == 'There. Hi'
    print('test is passed')

if __name__ == '__main__':
    assert reverse2('Hi There.') == 'There. Hi'
    print('test is passed')

if __name__ == '__main__':
    assert reverse3('Hi There.') == 'There. Hi'
    print('test is passed')