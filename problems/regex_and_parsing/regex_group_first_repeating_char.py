# Detects and prints the first alphanumeric character that appears consecutively using regex, or -1 if none exists.

import re

S = input()
m = re.search(r'([a-zA-Z0-9])\1+',S)

if m:
    print(m.group(1))
    
else:
    print(-1)