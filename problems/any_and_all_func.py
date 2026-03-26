# any() - This expression returns True if any element of the iterable is true. 
# If the iterable is empty, it will return False.
# all() - This expression returns True if all of the elements of the iterable are true. 
# If the iterable is empty, it will return True.

N = int(input())
numbers = list(map(int, input().split()))
print(all(num > 0 for num in numbers) and any(str(num) == str(num)[::-1] for num in numbers))