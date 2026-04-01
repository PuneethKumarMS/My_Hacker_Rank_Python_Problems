def rotateRight(d, arr):
    n = len(arr)
    d = d % n   
    rotation = arr[-d:] + arr[:-d]
    return rotation

if __name__ == '__main__':

    multiple_input = input().rstrip().split()
    d = int(multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = rotateRight(d, arr)
    print(*result)