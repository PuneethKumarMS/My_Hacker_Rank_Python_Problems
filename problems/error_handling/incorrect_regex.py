# Check whether a given string is a valid regular expression using re.compile() and exception handling.

import re 

n = int(input())

for i in range(n):
    s = input()
    try:
        re.compile(s)
        print('True')
        
    except re.error:
        print('False')