def simpleArraySum(arr):
    total = 0
    for num in arr:
        total +=num
    return total

if __name__ == '__main__':
    
    ar_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = simpleArraySum(arr)

    print(result)