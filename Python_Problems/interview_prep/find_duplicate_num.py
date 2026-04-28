n = int(input())

arr = list(map(int, input().split()))

found = False

for i in range(n):
    for j in range(i + 1, n):

        if arr[i] == arr[j]:
            print(arr[i])
            found = True
            break

    if found:
        break

if not found:
    print(-1)