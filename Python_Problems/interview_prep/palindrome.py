n = int(input()) 

if n < 0:
    print('Not Palindrome')

else:

    temp = n # to store number because number will modify after loop
            # So we need to compare this stored number with reversed number

    rev = 0 

    while n > 0:       
        digit = n % 10       
        rev = rev * 10 + digit 
        n = n // 10   

    if  rev == temp :
        print('Palindrome')
        
    else:
        print('Not Palindrome')