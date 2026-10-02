n = int(input())
zeros=0
negatives=0
pozitives_sum=0
pozitives_kolvo=0
for i in range(n):
    num=int(input())
    if num==0:
       zeros=zeros+1
    elif num<0:
        negatives=negatives+1
    elif num>0:
        positives_sum=pozitives_sum+num
        positives_kolvo=pozitives_kolvo+1

srednee=pozitives_sum/pozitives_kolvo

print(f"Нулей:zeros")
print(f"Отрицательных:negatives")
print(f"Среднее положительных:srednee")



