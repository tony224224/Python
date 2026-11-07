def max_digit(n):
    if n < 10:
        return n
    last_digit = n % 10
    max_in_rest = max_digit(n // 10)
    return max(last_digit, max_in_rest)

n = int(input())
print(max_digit(n))