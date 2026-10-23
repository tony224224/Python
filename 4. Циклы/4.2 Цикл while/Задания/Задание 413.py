max_val=0
pos_first=0
pos_last=0
current_pos=0
while (n := int(input())) != 0:
    current_pos += 1
    if n > max_val:
        max_val = n
        pos_first = current_pos
        pos_last = current_pos
    elif n == max_val:
        pos_last = current_pos
print(pos_first, pos_last)

