def rotateString(d, string):

    l = len(string)
    d = d % l
    r = string[d:] + string[:d]
    return r

if __name__ == '__main__':

    multiple_input = input().split()
    string = multiple_input[0]
    d = int(multiple_input[1])
    result = rotateString(d, string)
    print(result)