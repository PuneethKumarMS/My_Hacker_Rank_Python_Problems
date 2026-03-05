# Find and print the symmetric difference of two sets in ascending order (one element per line)

_ = int(input())
m = set(map(int, input().split()))

_ = int(input())
n = set(map(int, input().split()))

sym_diff = sorted(m.symmetric_difference(n))

for i in sym_diff:
    print(i)