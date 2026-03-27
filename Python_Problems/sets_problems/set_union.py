# Find the total number of unique students who subscribed to at least one newspaper using set union

_ = int(input())
english_student_roll_no = set(map(int, input().split()))

_ = int(input())
french_student_roll_no = set(map(int, input().split()))

combine = english_student_roll_no.union(french_student_roll_no)
print(len(combine))