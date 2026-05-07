arr = list(map(int, input().split()))

visited = []

for i in arr:
   if i in visited: 
      continue    # to skip visited element
   
   count = 0

   for j in arr: 
      
      if i == j:
         count += 1

   print(i, '->', count)

   visited.append(i)