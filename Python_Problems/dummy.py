n = int(input())
rev = 0

while n > 0:
    digit = n % 10
    #print(digit)
    rev = rev * 10 + digit
    print(rev)
    n = n // 10
    #print(n)
print(rev)
