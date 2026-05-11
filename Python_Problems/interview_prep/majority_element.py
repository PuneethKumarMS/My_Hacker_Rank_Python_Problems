# Find element occurring more than half of array size

n = int(input())

arr = list(map(int, input().split()))

visited = []

found = False

for i in arr:

    if i in visited:
        continue

    count = 0

    for j in arr:
        if i == j:
           count += 1

    if count > n//2:
        print(i)
        found = True
        break

    
if not found:
    print(-1)
          
    
    