#1, 5, 7, 11
import numpy as np


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

