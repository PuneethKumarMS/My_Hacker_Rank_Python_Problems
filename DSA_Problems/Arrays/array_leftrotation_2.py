# A left rotation operation on a circular array shifts each of the array's elements  unit to the left. 

def rotateLeft(no_of_rotations, arr):

    for _ in range(no_of_rotations):
        first = arr.pop(0) #removes first element of a list
        add = arr.append(first) #adds the removed element to the end of the list
    return arr

if __name__ == '__main__':

    multiple_input = input().rstrip().split()

    no_of_elements = int(multiple_input[0])
    no_of_rotations = int(multiple_input[1])
    
    arr = list(map(int, input().rstrip().split()))
    result = rotateLeft(no_of_rotations, arr)
    print(*result)