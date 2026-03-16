

from collections import namedtuple

no_of_students = int(input())
headers = input().split()
students = namedtuple('student_details', headers)
total = 0

for i in range(no_of_students):
    row = input().split()
    S = students(*row)
    total += int(S.MARKS)
    
print(f'{total/no_of_students:.2f}' )