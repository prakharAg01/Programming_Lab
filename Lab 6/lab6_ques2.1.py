#Find the sum of the following series for N terms 
#1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + ….. N terms.
n = int(input())
sum = 0 
i = 2
while i <= n:
    sum = sum + (1/i)
    i += 1
print("Sum :{:.9f}".format(sum+1))