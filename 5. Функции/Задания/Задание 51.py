from dis import code_info

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


n = int(input())
count = 0                               # сколько мы нашли
current_number = 2                      # текущее число
while count < n:
    if is_prime(current_number):        # передача текущего числа на проверку в is_prime()
        print(current_number, end=' ')
        count += 1
        current_number += 1
