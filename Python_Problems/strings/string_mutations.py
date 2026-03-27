# Replace a character in a string using slicing because strings are immutable.
# Take the part before the given index, add the new character, and then
# add the remaining part of the string after that index.

def mutate_string(string, position, character):
    new = string[:position] + character + string[position + 1 :]
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)