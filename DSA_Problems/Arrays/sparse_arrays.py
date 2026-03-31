# Count how many times each query string appears in the given string list

def matchingSrings(stringList, queries):
    total = []
    for string in queries:
        total.append(stringList.count(string))
        
    return total

if __name__ == '__main__':
    
    stringList_count = int(input().strip())
    stringList = []
    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    result = matchingSrings(stringList, queries)
    print(*result, sep='\n')