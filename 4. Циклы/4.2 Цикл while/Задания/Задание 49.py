total_sum = 0
count = 0
while (n := int(input())) != 0:
    total_sum = total_sum + n
    count = count + 1
average = total_sum / count
print(average)
