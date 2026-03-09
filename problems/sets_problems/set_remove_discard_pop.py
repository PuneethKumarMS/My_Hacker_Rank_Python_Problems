# Execute pop, remove, and discard operations on a set based on given commands and print the final sum of elements

n = int(input())
s = set(map(int, input().split()))

m = int(input())

for _ in range(m):
    cmd = input().split()
    
    if cmd[0] == 'pop'.lower():
        s.pop()
        
    elif cmd[0] == 'remove'.lower():
        s.remove(int(cmd[1]))
    
    elif cmd[0] == 'discard'.lower():
        s.discard(int(cmd[1]))
        
print(sum(s))