n = int(input())
a = 0
b = 1

for _ in range(n):
    print(a)
    nxt = a + b
    a = b 
    b = nxt

