n = int(input())
lst = list(map(int, input().split()))
mid = n // 2
result= lst[:mid][::-1] + lst[mid:][::-1]
print(*result)
