# Repeatedly sum the digits of a number until it becomes a single digit

N = int(input())

while N >= 10: # Outer loop: repeat the digit-summing process until the number becomes a single digit

    total = 0

    while N > 0:     # Inner loop: calculate the sum of digits of the current number
        digit = N % 10
        total += digit
        N = N // 10
    
    N = total

print(N)