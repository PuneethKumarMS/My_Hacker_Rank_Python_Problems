n = int(input())
arr = list(map(int, input().split())) # array in n-1 

expected_sum = n*(n+1)//2

total_arr = 0

for num in arr:
    total_arr += num

print(expected_sum - total_arr)





