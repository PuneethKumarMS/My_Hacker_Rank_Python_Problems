n = int(input())

arr = list(map(int, input().split()))

squares = []

for i in arr:

    s = i ** 2
    squares.append(s)

squares.sort()
print(squares)


