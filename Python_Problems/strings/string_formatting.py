# Print numbers from 1 to n in decimal, octal, hexadecimal, and binary formats aligned to the width of n's binary representation.

def print_formatted(number):
    
    for i in range(1, n + 1):
        dec = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        width = len(bin(n)[2:])
        
        print(dec.rjust(width),
              octal.rjust(width),
              hexadecimal.rjust(width),
              binary.rjust(width))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)