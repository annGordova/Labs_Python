s = input()
a = s.split()
st = set()
for x in a:
    if x not in st:
        print('NO')
        st.add(x)
    else:
        print('YES')