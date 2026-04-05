# reverse an array of integers.

def reverseArray(a):
    a = a[::-1]
    return a


if __name__ == '__main__':

    arr_count = int(input().strip())
    arr =  list(map(int, input().strip().split()))
    res = reverseArray(arr)
    print(*res)
