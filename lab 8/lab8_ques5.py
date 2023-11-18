#1
'''N = int(input("enter a number : "))
lst = []
sum = 0
for i in range(N):
    a = str(input("Enter a string : "))
    lst.append(a)
print(lst)
b = str(input("Enter sample string : "))
for j in lst:
    if j == b :
        sum += 1
print(sum)'''


#2
'''N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = int(input("Enter a number : "))
    lst.append(a)
print(lst)
new = []
for i in lst:
    if i > 0:
        new.append(i**2)
    else:
        new.append(0)
print("modified list :",new)'''

#3
N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = int(input("Enter a number : "))
    lst.append(a)
print(lst)
new = []
for i in lst:
    if i >= 10 and i <= 20 :
        new.append(i**2)
    else:
        new.append(i)
print("modified list :",new)

#4
