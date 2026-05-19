# print true if the number is float or else print false

t = int(input())

for i in range(t):
    n = input()
    if '.' in n:  # to check decmals
        try:
            f = float(n)
            print(True)
        except:
            print(False)
    else:
        print(False)
