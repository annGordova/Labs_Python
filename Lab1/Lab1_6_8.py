

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
