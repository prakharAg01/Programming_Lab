N = int(input("enter a number : "))
sum = 0 
pro = 1
lst = []
for i in range(N):
    A = int(input())
    lst.append(A)
print(lst)
for i in lst :
    sum = sum + i
print("sum :",sum)
for j in lst:
    pro = pro * j
print("Product :",pro)
#for max 
num = lst[0]
for k in lst:
    if num < k :
        num = k 
print("Largest number :",num)
