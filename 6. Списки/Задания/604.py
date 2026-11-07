lst = list(map(int, input().split()))
num_min = lst.index(min(lst))
num_max = lst.index(max(lst))
lst[num_min] , lst[num_max] = lst[num_max] , lst[num_min]
print(*lst)
