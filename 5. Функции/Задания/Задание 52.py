def is_perfect(n):
    total_sum=0
    for i in range(1,n):
        if n % i == 0:
            total_sum += i
    return total_sum == n

n = int(input())
count =0
current_number = 2
while count < n:
    if is_perfect(current_number):
        print(current_number, end=' ')
        count += 1
    current_number += 1



