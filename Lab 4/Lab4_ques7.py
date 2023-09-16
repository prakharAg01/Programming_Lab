#to display first N terms of fibonacci sequence starting from 1
N = int(input())
a = 0
b = 1
while b <= N:
    print(b)
    temp = b
    b = a + b
    a = temp