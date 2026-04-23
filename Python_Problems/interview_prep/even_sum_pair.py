# My TCS NQT problem

n = int(input())

even_count = 0

for i in range(1, n+1):
    for j in range(i, n+1):

        if (i + j) % 2 == 0:
            even_count += 1

print(even_count)