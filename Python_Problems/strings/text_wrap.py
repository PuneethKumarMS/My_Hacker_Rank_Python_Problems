# Wrap a string into lines of fixed width using range() stepping and string slicing

def wrap(string, max_width):
    wrapped = ''

    for i in range(0, len(string),  max_width):
        ch = string[i : i + max_width ]
        wrapped += ch + '\n'
    return wrapped

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)