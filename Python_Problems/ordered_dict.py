# Store item and add prices, keeping the same input order.

from collections import OrderedDict

N = int(input())
d = OrderedDict()

for i in range(N):
    parts = input().split()
    price = int(parts[-1])
    item = ' '.join(parts[:-1])
    
    if item in d:
        d[item] += price
    else:
        d[item] = price

for item in d:
    print(item, d[item])