def sum_seq(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s

start = 50
finish = 100
print(sum_seq(50, finish))