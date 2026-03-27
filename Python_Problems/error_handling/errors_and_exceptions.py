# Perform division for multiple inputs and handle errors like invalid input or divide-by-zero using try-except
a = int(input())

for i in range(a):
    c,d= input().split()
    try :
        c,d= map(int, input().split())
        division = c//d
        print(division)
        
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')        
    except ValueError as e:
        print('Error Code:',e)