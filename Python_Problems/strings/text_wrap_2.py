# Use textwrap.fill() to automatically wrap a string into lines of a specified width

import textwrap

def wrap(string, max_width):

    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)