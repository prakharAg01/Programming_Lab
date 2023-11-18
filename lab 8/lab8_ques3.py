'''Take a list of integers as input and sort the elements of the list in-place, i.e., do not use any
other list for storing the result, only the values in the list are swapped to form the sorted list.
(Do not use the inbuilt sorting function).'''
N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
print(lst)

for j in range(N):
