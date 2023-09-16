#to display sum of digits of number N
N = int(input())
sum = 0
if N <= 0:
    print("Invalid Inputs") 
while N > 0:
    num = N%10
    sum = sum + num
    N = N//10
print(sum)
