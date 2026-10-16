start_sum = int(input())
target_sum = int(input())
percent = int(input())
current_sum = start_sum
montly_persent = percent / 12
month=1
while current_sum <= target_sum:
    current_sum = current_sum * (1 + montly_persent / 100)
    print(f"{month} - {current_sum:.2f}")
    month += 1