n = int(input())
last =n % 10
last2 = n % 100
if 11<= last2 <=14:
    print("грибов")
elif last == 1:
    print("гриб")
elif 2 <= last <= 4:
    print("гриба")
else:
    print("грибов")
