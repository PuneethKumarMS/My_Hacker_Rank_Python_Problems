# any() returns True if at least one element in an iterable is True, otherwise False.
# Here it checks each character of the string and returns True if any character
# is alphanumeric, alphabetic, digit, lowercase, or uppercase.

if __name__ == '__main__':
    s = input()
    
    print(any(ch.isalnum() for ch in s ))
    print(any(ch.isalpha() for ch in s))
    print(any(ch.isdigit() for ch in s))
    print(any(ch.islower() for ch in s))
    print(any(ch.isupper() for ch in s))