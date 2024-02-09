def Comparator(s):
    s_l = s.split()
    return len(s_l)
n = int(input('Введите число строк: '))
print('Введите строки')
a = [input() for i in range(n)]
a.sort(key=Comparator)
print('Упорядоченный по кол-ву слов в строке:')
print(a)