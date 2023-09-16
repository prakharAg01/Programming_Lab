#to input 3 numbers and check if the sum of
#their digits is divisible by 3.
num = int(input("Enter 3 digit number : "))
A = num//100
B = num%100
C = B//10
D = B%10
sum = A+C+D
print(sum)
if sum%3 == 0 :
    print("Sum of digits is divisible by 3")
else:
    print("Sum of digits is not divisible by 3")