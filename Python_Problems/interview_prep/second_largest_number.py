n = int(input())
arr = list(map(int, input().split()))

arr.sort()

largest = arr[-1]

for i in range(n-2, -1, -1):
    if arr[i] != largest:
        print(arr[i])
        break
else:
    print(-1)