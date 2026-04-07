n = int(input())   # take input number
rev = 0            # this will store the reversed number

while n > 0:       # run loop until all digits are removed
    digit = n % 10         # extract last digit (e.g., 123 % 10 = 3)
    
    rev = rev * 10 + digit # shift rev left and add digit
                           # example: rev=32 → 320 + 1 = 321
    
    n = n // 10            # remove last digit from n
                           # example: 123 → 12

print(rev)          # print final reversed number