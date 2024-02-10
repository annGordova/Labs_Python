#1, 5, 7, 11
import numpy as np
class No_num(Exception):
    pass

def f1(s):
    gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    k_gl, k_sogl = 0, 0
    for x in s:
        if x in gls:
            k_gl += 1
        else:
            k_sogl += 1
    return abs(k_gl-k_sogl)


def calculate_deviation_f5(string, average_frequencies):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    max_char = max(char_counts, key=char_counts.get)
    max_frequency = char_counts[max_char] / len(string)

    deviation = (max_frequency - average_frequencies[max_char]) ** 2
    return deviation


def sort_strings_f5(strings, average_frequencies):
    return sorted(strings, key=lambda x: calculate_deviation_f5(x, average_frequencies))

def f7(s):
    gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    k_gs, k_sg = 0, 0
    for i in range(0, len(s)-1):
        if s[i] in gls and s[i+1] not in gls:
            k_gs += 1
        elif s[i] not in gls and s[i+1] in gls:
            k_sg += 1
    return abs(k_gs - k_sg)


def max_average_ascii_weight_f11(s):
    max_avg_weight = 0
    for i in range(len(s) - 2):
        avg_weight = sum(ord(c) for c in s[i:i + 3]) / 3
        max_avg_weight = max(max_avg_weight, avg_weight)
    return max_avg_weight


def sort_strings_by_deviation_f11(strings):
    base_max_avg_weight = max_average_ascii_weight_f11(strings[0])
    def deviation(s):
        return (max_average_ascii_weight_f11(s) - base_max_avg_weight) ** 2
    return sorted(strings, key=deviation)


print('Введите номер задачи: 1, 5, 7 или 11')
num = int(input())
try:
    if num not in [1, 5, 7, 11]:
        raise No_num
except No_num:
    print('Ошибка')

if num != 5:
    n = int(input('Введите число строк: '))
    print('Введите строки')
    a = [input() for i in range(n)]

if num == 1:
    a.sort(key=f1)
    print('Сортировка в порядке увеличения разницы между количеством согласных и количеством гласных букв в кириллице')
    print(a)
elif num == 5:
    print('Сортировка по квадратичному отклонению строк example, test, hello')
    strings = ["example", "test", "hello"]
    #не реализовала ввод произвольных строк, чтобы не задавать словарь частоты встречаемости для всех латинских букв, однако это можно сделать, алгоритм не поменяется
    average_frequencies = {'e': 0.1, 'x': 0.05, 'a': 0.08, 'm': 0.04, 'p': 0.02, 'l': 0.04, 't': 0.09, 's': 0.06, 'h': 0.05, 'o': 0.07}
    sorted_strings = sort_strings_f5(strings, average_frequencies)
    print(sorted_strings)
elif num == 7:
    a.sort(key=f7)
    print('Сортировка в порядке увеличения разницы между количеством сочетаний «гласная-согласная» и «согласная-гласная» в кириллице')
    print(a)


elif num == 11:
    print('Сортировка по квадратичному отклонению дисперсии')
    sorted_strings = sort_strings_by_deviation_f11(a)
    print(sorted_strings)