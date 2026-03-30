def simpleArraySum(ar):
    add =  sum(ar)
    return add

if __name__ == '__main__':
    
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)