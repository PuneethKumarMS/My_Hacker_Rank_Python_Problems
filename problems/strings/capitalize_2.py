# Split the string by spaces, capitalize each word, and join them back into a single string.

def solve(s):

    print(' '.join(ch.capitalize() for ch in s.split(' ')))
    
if __name__ == '__main__':

    s = input()

    result = solve(s)