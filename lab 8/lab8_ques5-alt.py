#2
'''N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = int(input("Enter a number : "))
    lst.append(a)
print(lst)

new = [0 if i < 0 else i**2 for i in lst]
print(new)'''

#3
N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = int(input("Enter a number : "))
    lst.append(a)
print(lst)

new = [i ** 2 if i >= 10 and i <= 20 else i for i in lst]
print(new)

#4
'''N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = str(input("Enter a number : "))
    lst.append(a)
print(lst)

new = [i.title() if not i.istitle() else i for i in lst ]
print(new)'''