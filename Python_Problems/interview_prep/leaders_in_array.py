# An element is called a leader if it is greater than all elements to its right.

n = int(input())

arr = list(map(int, input().split()))

leaders = []

max_from_right = arr[-1]

for i in range(n-1, -1, -1):
    if arr[i] >=  max_from_right:  # last element iteslf is leader
        leaders.append(arr[i])
        max_from_right = arr[i] # arr[i] is stored to max after comparing
    
print(leaders[::-1])
