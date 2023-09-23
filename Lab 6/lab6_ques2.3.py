#Find the sum of the following series for N terms
#F(x) = 1 + x/1 + x2/2 + x3/3 + x4/4 + ….. + N terms (Take x also as input)
N = int(input("Enter number of terms : "))
x = int(input("Enter value of x : "))
i = 1
sum = 0
while i <= N:
    sum = float(sum) + ((x**(i))/i)
    i += 1
print("Sum :{:.9f}".format(sum+1))