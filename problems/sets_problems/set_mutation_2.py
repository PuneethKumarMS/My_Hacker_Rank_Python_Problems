# This program performs mutation operations on a set based on input commands
# (update, intersection_update, difference_update, symmetric_difference_update)
# and prints the final sum of elements in the set.

# getattr(object, method_name) dynamically fetches a method using its name as a string.
# Here, getattr(A, operation_name)(other_set) works like A.update(other_set) or
# A.intersection_update(other_set) depending on the operation given in the input.

_ = int(input())
A = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    operation = input().split()
    other_set = set(map(int, input().split()))
    getattr(A, operation[0])(other_set)
    
print(sum(A))