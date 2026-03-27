N = int(input())
repeated_words = {}

for i in range(N):
    word = input()
    
    if word in repeated_words:
        repeated_words[word] += 1
        
    else:
        repeated_words[word]= 1
        
print(len(repeated_words))
print(*repeated_words.values())