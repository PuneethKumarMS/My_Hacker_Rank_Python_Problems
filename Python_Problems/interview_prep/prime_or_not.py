# A number is prime if it has exactly two divisors: 1 and itself

N = int(input())

if N <= 1:
    print('Not prime')

else:
    for i in range(2, N):
        if N % i == 0:
            print('Not prime')
            break
    else:
        print('Prime')