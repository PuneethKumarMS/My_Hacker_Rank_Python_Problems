# Sell the shoe if the requested size is available and decrease its stock while adding the price to total earnings.

from collections import Counter # Import Counter to count and track how many shoes are available for each size and it act as dictionary

no_of_shoes = int(input())
list_of_shoe_sizes = Counter(list(map(int, input().split())))
no_of_customers = int(input())
total = 0

for i in range(no_of_customers):
    size, price = map(int, input().split())
    
    if list_of_shoe_sizes[size] > 0:
        total += price
        list_of_shoe_sizes[size] -= 1
print(total) 
