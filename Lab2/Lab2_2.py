n = int(input())
a = []
d = {}
for i in range(n):
    s = input()
    ai = s.split()
    a += ai
    for x in ai:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1

mx = -1
slovo = ''
for x in d:
    if d[x] > mx:
        mx = d[x]
        slovo = x
    elif d[x] == mx:
        if x < slovo:
            slovo = x
print(slovo)