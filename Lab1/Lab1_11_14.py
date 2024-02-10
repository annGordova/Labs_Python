#1, 5, 7, 11
import numpy as np



def f7(s):
    gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    k_gs, k_sg = 0, 0
    for i in range(0, len(s)-1):
        if s[i] in gls and s[i+1] not in gls:
            k_gs += 1
        elif s[i] not in gls and s[i+1] in gls:
            k_sg += 1
    return abs(k_gs - k_sg)


