n = int(input())
zeros = 0
negatives = 0
positives_sum = 0
positives_count = 0
for i in range(n):
    num = int(input())
    if num == 0:
        zeros = zeros + 1
    elif num < 0:
        negatives = negatives + 1
    elif num > 0:
        positives_sum = positives_sum + num
        positives_count = positives_count + 1

average = positives_sum / positives_count

print(f"Нулей:zeros")
print(f"Отрицательных:negatives")
print(f"Среднее положительных:average")
