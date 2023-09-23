#Find the sum of the following series for N terms
#1/1! + 1/2! + 1/3! + 1/4! + … + 1/N! 
N = int(input())
i = 1
fact = 1
sum = 0
while i <= N:
    fact = fact*i
    sum = sum + (1/fact)
    i += 1
print("Sum :{:.9f}".format(sum))