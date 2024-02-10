#4, 16, 28, 40, 52

class item_with_num_f4:
    def __init__(self, item, num):
        self.item = item
        self.num = num
    def __lt__(self, other):
        return self.item > other.item

    def get_num(self): return self.num

def f4(a):
    a_items = []
    for i in range(0, len(a)):
        a_items.append(item_with_num_f4(a[i], i))
    a_items.sort()
    ind = []
    for x in a_items:
        ind.append(x.get_num())
    return ind
