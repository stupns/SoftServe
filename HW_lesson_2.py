# Записати в стрічку філософію Пайтона
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Замінити всі входження символу “і” на “&”
with open('/usr/lib/python3.6/this.py') as file:
    int_num = file.read()
    new_int = str(int_num[4:866])
    d = {}
    for new_int in (65, 97):
        for i in range(26):
            d[chr(i + new_int)] = chr((i + 13) % 26 + new_int)
    result = ''.join(d.get(new_int, new_int) for new_int in int_num)
text = result[3:867]


def func_one(text: str):
    task1 = 'better : {}, never : {}, is : {}'.format(text.count('better'), text.count('never'), text.count('is'))
    task2 = text.upper().replace('I', '&')
    print(task1 + '\n' + task2)


func_one(text)

