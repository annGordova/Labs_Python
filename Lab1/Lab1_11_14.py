#1, 5, 7, 11
import numpy as np


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

