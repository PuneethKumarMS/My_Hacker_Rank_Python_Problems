# Apply multiple mutation operations on set A and print the sum of the final elements.

_ = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation = input().split()
    other_set = set(map(int, input().split()))

    if operation[0] == 'intersection_update':
        A.intersection_update(other_set)
        
    elif operation[0] == 'update':
        A.update(other_set)
        
    elif operation[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(other_set)
        
    elif operation[0] == 'difference_update':
        A.difference_update(other_set)

print(sum(A))



