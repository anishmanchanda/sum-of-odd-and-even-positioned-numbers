#sum of odd and even positioned numbers seperately
n = int(input("enter number of numbers"))
list=[]
sumeven=0
sumodd=0
for i in range(1,n+1):
    num = int(input("enter a number"))
    list.append(num)
for j in range(len(list)):
    if j%2==0:
        sumeven=sumeven + list[j]
    else:
        sumodd=sumodd+list[j]

print(list)
print("sum of even positioned is",sumeven)
print("sum of odd p[ositioned is", sumodd)
