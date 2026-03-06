# Find the number of students who have subscribed to both English and French newspapers using set intersection.

_ = int(input())
english_newspaper = set(map(int, input().split()))

_ = int(input())
french_newspaper = set(map(int, input().split()))

intersections = english_newspaper.intersection(french_newspaper)
print(len(intersections))