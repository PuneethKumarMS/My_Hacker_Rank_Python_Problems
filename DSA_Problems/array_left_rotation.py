# A left rotation operation on a circular array shifts each of the array's elements  unit to the left. 

def rotateLeft(d, arr):
    d = d % len(arr)
    rotation = arr[d:] + arr[:d] 
    return rotation

if __name__ == '__main__':

     multiple_input = input().rstrip().split()
     n = int(multiple_input[0])
     d = int(multiple_input[1])  # no_of_rotation

     arr = list(map(int, input().rstrip().split()))

     result = rotateLeft(d, arr)
     print(*result)