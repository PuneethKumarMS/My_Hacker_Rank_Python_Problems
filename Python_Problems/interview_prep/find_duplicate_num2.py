n = int(input())

arr = list(map(int, input().split()))

seen = []

for num in arr:

    if num in seen:
        print(num)
        break
    seen.append(num)

else:
    print(-1)