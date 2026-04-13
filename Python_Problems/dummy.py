N = int(input())
temp = N
total = 0

if N <= 1:
    print('Not perfect')

else:
    for i in range(1, N):

        if N % i == 0:
            total += i
    print('Perfect' if temp == total  else 'Not Perfect')