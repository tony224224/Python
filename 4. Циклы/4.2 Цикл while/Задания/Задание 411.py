max_num = 1
count = 1
while (n := int(input())) != 0:
    if n > max_num:
        max_num = n
        count = 1
    elif n == max_num:
        count += 1
print(count)