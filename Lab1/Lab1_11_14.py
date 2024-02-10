#1, 5, 7, 11
import numpy as np


def f1(s):
    gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    k_gl, k_sogl = 0, 0
    for x in s:
        if x in gls:
            k_gl += 1
        else:
            k_sogl += 1
    return abs(k_gl-k_sogl)

