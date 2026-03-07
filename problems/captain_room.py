# Find the Captain's room number where all family room numbers appear k times but the Captain's appears only once.

# k = int(input())
# room_numbers = list(map(int, input().split()))

# for room in set(room_numbers):
#     counting = room_numbers.count(room)

#     if counting == 1:
#         print(room)

k = int(input())
rooms = list(map(int, input().split()))

captain = (sum(set(rooms)) * k - sum(rooms)) // (k - 1)

print(captain)