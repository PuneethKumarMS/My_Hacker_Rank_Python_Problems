# Enter your code here. Read input from STDIN. Print output to STDOUT

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