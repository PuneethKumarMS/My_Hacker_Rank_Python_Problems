t = int(input())

for _ in range(t):
    _ = int(input())  # size of A
    A = set(map(int, input().split()))
    
    _ = int(input())  # size of B
    B = set(map(int, input().split()))
    
    print(A.issubset(B))