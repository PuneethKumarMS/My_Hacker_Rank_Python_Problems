def rotateLeft(d, arr):
    rotation = arr[d:] + arr[:d]
    return rotation

if __name__ == '__main__':

     multiple_input = input().rstrip().split()
     n = int(multiple_input[0])
     d = int(multiple_input[1])

     arr = list(map(int, input().rstrip().split()))

     result = rotateLeft(d, arr)
     print(*result)