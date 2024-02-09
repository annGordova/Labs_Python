def Vs_Simple_f1_f3(x, y):
    for i in range(2, min(x, y)+1):
        if x%i == 0 and y %i == 0:
            return False
    return True

def f1(x):
    k = 0
    for i in range(2, x, 2):
        if not(Vs_Simple_f1_f3(i, x)):
            k += 1
    return k
