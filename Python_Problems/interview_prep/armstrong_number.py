# A number is Armstrong if sum of digits raised to power of digit count equals the number

n = int(input())

original = n
temp = n

count_of_n = 0
sum = 0

if n == 0:
    count_of_n = 1

while temp > 0:
    temp = temp//10
    count_of_n += 1

while n > 0:
    digit = n % 10
    sum += digit ** count_of_n
    n = n // 10

print('Armstrong' if sum == original else 'Not Armstrong')

'''
This code only applicable for 3 digit number

import math

n = int(input())
temp = n
sum = 0

while n != 0:
    digit = n % 10
    sum += digit * digit * digit
    n //= 10

print("Armstrong" if temp == sum else "Not Armstrong")
'''