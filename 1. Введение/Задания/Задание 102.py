from math import sqrt
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
a = (sqrt((x2-x1)**2 + (y2-y1)**2))
b = (sqrt((x3-x2)**2 + (y3-y2)**2))
c = (sqrt((x3-x1)**2 + (y3-y1)**2))
perimeter = a+b+c
p = perimeter / 2
s1 = p * (p - a) * (p - b) * (p - c)
s = (sqrt(s1))
print(perimeter)
print(s)
