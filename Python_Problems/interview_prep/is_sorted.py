def isSorted(N, arr):

    for i in range(N-1):
        if arr[i] > arr[i+1]:
            return 'Not Sorted'
            break
    
    else:
        return 'Sorted'

if __name__ == '__main__':

    N = int(input())
    arr = list(map(int, input().split()))

    result = isSorted(N, arr)
    print(result)

    
