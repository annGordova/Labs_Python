n = int(input('Введите число строк: '))
print('Введите строки')
a = [input() for i in range(n)]
a.sort(key=len)
print('Упорядоченный по длине строк:')
print(*a)