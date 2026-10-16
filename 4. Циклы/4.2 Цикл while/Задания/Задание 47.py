n = int(input())
sum = 0
while n > 0:
    s = n % 10
    sum += s
    n //= 10
print(sum)
