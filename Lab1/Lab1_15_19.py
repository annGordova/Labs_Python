

def Simple_f52(x):
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def f52(x):
    a = []
    while not(Simple_f52(x)):
        for i in range(2, x):
            if x%i==0:
                a.append(i)
                x//=i
                break
    a.append(x)
    return a
