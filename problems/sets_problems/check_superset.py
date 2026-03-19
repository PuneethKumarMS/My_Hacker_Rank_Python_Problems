# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))

N = int(input())

result = True

for _ in range(N):
    B = set(map(int, input().split()))
    
    if not A > B:   # check strict superset
        result = False

print(result)
