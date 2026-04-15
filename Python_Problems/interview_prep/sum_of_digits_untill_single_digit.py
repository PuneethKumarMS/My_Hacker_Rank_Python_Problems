N = int(input())

while N >= 10:
    total = 0

    while N > 0:

        digit = N % 10
        total += digit
        N = N // 10
    
    N = total

print(N)