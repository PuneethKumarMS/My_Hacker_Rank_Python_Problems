# A number is Strong if sum of factorials of its digits equals the number

N = int(input())

temp = N # to stores the original Number

total = 0 # stores the sum of factorial of each digit 

if N == 0:
    print('Not Strong')

else:

    while N > 0:
        digit = N % 10 # to get last digit of number
        fact = 1 

        for i in range(1, digit+1): # loop to calculate factorial
            fact *= i
        
        total += fact 

        N = N // 10  # to remove last digit of a number in each step

    print('Strong' if temp == total else 'Not Strong')