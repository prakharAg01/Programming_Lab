N = int(input("enter a number : "))
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)
print(lst)
#Take a list of integers as input and sort the elements of the list by taking another list and
#incrementally appending values in the 2nd list. (Do not use the inbuilt sorting function).
sorted_lst = []
while lst:
    minimum = lst[0]
    for j in lst:
        if j < minimum:
            minimum = j
    sorted_lst.append(minimum)
    lst.remove(minimum)
print(sorted_lst)
