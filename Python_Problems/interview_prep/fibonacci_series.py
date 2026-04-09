n = int(input())
a = 0
b = 1

for _ in range(n):
    print(a, end=" ") # to print in a single line
    nxt = a + b
    a = b 
    b = nxt

