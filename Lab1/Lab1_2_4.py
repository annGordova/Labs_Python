class No_num(Exception):
    pass

def f4(s):
    if s == s[::-1]:
        print('Строка палиндром')
    else:
        print('Строка не палиндром')

def f11(s):
    a = s.split()
    print('Число слов ' + str(len(a)))

def f15(x):
    print('Число различных символов ' + str(len(set(str(x)))))

print('Введите номер задачи: 4, 11 или 15')
num = int(input())
try:
    if num not in [4, 11, 15]:
        raise No_num
except No_num:
    print('Ошибка')


if num == 4:
    si = input('Введите строку ')
    f4(si)
elif num == 11:
    si = input('Введите строку ')
    f11(si)
elif num == 15:
    xi = input('Введите число ')
    f15(xi)