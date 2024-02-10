#4, 16, 28, 40, 52
class No_num(Exception):
    pass
class item_with_num_f4:
    def __init__(self, item, num):
        self.item = item
        self.num = num
    def __lt__(self, other):
        return self.item > other.item

    def get_num(self): return self.num

def f4(a):
    a_items = []
    for i in range(0, len(a)):
        a_items.append(item_with_num_f4(a[i], i))
    a_items.sort()
    ind = []
    for x in a_items:
        ind.append(x.get_num())
    return ind

def f16(a):
    m1 = max(a)
    m2 = -10*10
    for x in a:
        if x != m1 and x > m2:
            m2 = x
    i1 = a.index(m1)
    i2 = a.index(m2)
    if i1 > i2:
        return a[i2+1:i1]
    else:
        return a[i1+1:i2]

def f28(a):
    mx = max(a)
    mn = min(a)
    imx = a.index(mx)
    imn = a.index(mn)
    if imn > imx:
        return a[imx+1:imn]
    else:
        return a[imn+1:imx]

def f40(a):
    return min(x for x in a if x%2==0)

def Simple_f52(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def f52(x):
    a = []
    while not(Simple_f52(x)):
        for i in range(2, x):
            if x%i==0:
                a.append(i)
                x//=i
                break
    a.append(x)
    return a

print('Введите номер задачи: 4, 16, 28, 40, 52')
num = int(input())
try:
    if num not in [4, 16, 28, 40, 52]:
        raise No_num
except No_num:
    print('Ошибка')



if num == 4:
    n = int(input('Введите длину массива '))
    print('Введите массив')
    a = [int(input()) for i in range(n)]
    print('Индексы массива в порядке,в котором эелменты образуют убывающую посл-ь')
    print(*f4(a))
elif num == 16:
    n = int(input('Введите длину массива '))
    print('Введите массив')
    a = [int(input()) for i in range(n)]
    print('Элементы между первым и вторым максимальным: ')
    print(*f16(a))
elif num == 28:
    n = int(input('Введите длину массива '))
    print('Введите массив')
    a = [int(input()) for i in range(n)]
    print('Элементы между минимальным и максимальным: ')
    print(*f28(a))
elif num == 40:
    n = int(input('Введите длину массива '))
    print('Введите массив')
    a = [int(input()) for i in range(n)]
    print('Минимальный четный элемент')
    print(f40(a))
elif num == 52:
    num = int(input('Введите число '))
    print('Разложение на простые делители')
    print(*f52(num))


