num = int(input())

num_list = list(str(num))   # convert to list
num_list.reverse()          # reverse function
reversed_num = int("".join(num_list))  # convert back

print(reversed_num)