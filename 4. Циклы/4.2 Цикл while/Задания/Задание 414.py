max_len = 0
current_len = 0
prev = 0
while (n := int(input())) != 0:
     if n == prev:
         current_len += 1
     else:
         current_len = 1
     if current_len > max_len:
         max_len = current_len
     prev = n
print(max_len)

