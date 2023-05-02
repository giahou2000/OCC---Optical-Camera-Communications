lst = [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1]

current_num = lst[0]
current_count = 1
groups = []

for num in lst[1:]:
    if num == current_num:
        current_count += 1
    else:
        groups.append((current_num, current_count))
        current_num = num
        current_count = 1

groups.append((current_num, current_count))

print(len(groups))
