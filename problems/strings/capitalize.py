# Split the name, capitalize the first letter of each word, and rebuild the string.

def solve(s):
    full_name = s.split(' ')
    result = ''
    
    for ch in full_name:
        if ch and ch[0].isalpha():
            upper_letter = ch[0].upper()
            other_letters = ch[1:]
            name = upper_letter  +  other_letters
            
        else:
            name = ch
        result += name + ' '
    print(result)
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
