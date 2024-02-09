class No_num(Exception):
    pass

def f4(s):
    a = s.split()
    k = 0
    for si in a:
        if int(si) < 5:
            k += 1
    return k

def f15(s):
    a = s.split()
    k = 0
    for si in a:
        if int(si) > 5:
            k += 1
    return k

def f11(s):
    i1 = ord('a')
    i1_e = ord('z')
    i2 = ord('A')
    i2_e = ord('Z')
    a1 = [chr(i) for i in range(i1, i1_e+1)]
    a2 = [chr(i) for i in range(i2, i2_e+1)]
    for x in s:
        if x in a1:
            a1.remove(x)
        if x in a2:
            a2.remove(x)
    print(*a1)
    print(*a2)

print('Введите номер задачи: 4, 11 или 15')
num = int(input())
try:
    if num not in [4, 11, 15]:
        raise No_num
except No_num:
    print('Ошибка')

if num == 4:
    si = input('Введите строку ')
    print('Количество чисел, меньших 5: ', f4(si))
elif num == 11:
    si = input('Введите строку ')
    print('Незадействоанные символы латиницы:')
    f11(si)
elif num == 15:
    si = input('Введите строку ')
    print('Количество чисел, больших 5: ', f15(si))