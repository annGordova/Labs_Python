import re
s = input()
a = re.findall(r'\d{2} \w{3,9} \d{4}' , s)
for x in a:
    print(x)