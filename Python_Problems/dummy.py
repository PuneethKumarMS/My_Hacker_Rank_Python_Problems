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