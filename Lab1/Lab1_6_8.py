

def f15(s):
    a = s.split()
    k = 0
    for si in a:
        if int(si) > 5:
            k += 1
    return k

