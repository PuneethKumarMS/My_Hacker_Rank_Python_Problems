# Traverse the string and swap the case of each character (upper → lower, lower → upper)

def swap_case(s):
    
    new_s = ''
    
    for ch in s:
        if ch.isupper():
            new_s += ch.lower()
            
        elif not ch.isupper:
            new_s += ch.upper()
            
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)