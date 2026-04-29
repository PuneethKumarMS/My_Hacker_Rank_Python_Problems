n = int(input())
arr = list(map(int, input().split()))

non_zero = []
zeroes = []

for i in arr:
    if i == 0:
        zeroes.append(i)

    elif i != 0:
        non_zero.append(i)

print(non_zero + zeroes)
