class No_num(Exception):
    pass

def f4(s):
    if s == s[::-1]:
        print('Строка палиндром')
    else:
        print('Строка не палиндром')
