n = int(input())

if n < 0:
    print("Not Armstrong")
    
else:
    s = str(n)              # convert number to string
    power = len(s)          # number of digits

    total = 0

    for digit in s:         # iterate through each character
        total += int(digit) ** power

    print("Armstrong" if total == n else "Not Armstrong")