#4, 16, 28, 40, 52


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




