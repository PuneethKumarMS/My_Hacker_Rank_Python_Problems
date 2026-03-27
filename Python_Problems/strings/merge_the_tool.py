# Split the string into parts of length k and remove repeated characters

def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):
        sl = string[i : i+k]
        result = ''
        
        for ch in sl:
            if ch not in result:
                result += ch
        print(result)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)