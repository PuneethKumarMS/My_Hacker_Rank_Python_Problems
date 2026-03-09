# Check whether set A is a subset of set B

t = int(input())

for _ in range(t):
    _ = int(input())  # size of A
    A = set(map(int, input().split()))
    
    _ = int(input())  # size of B
    B = set(map(int, input().split()))
    
    print(A.issubset(B))

     # or 
'''
t = int(input())

for _ in range(t):
    _ = int(input())  # size of A
    A = set(map(int, input().split()))
    
    _ = int(input())  # size of B
    B = set(map(int, input().split()))

    if A.union(B) == B:
        print(True)
    else:
        print(False)

'''