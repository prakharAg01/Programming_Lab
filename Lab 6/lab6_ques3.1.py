#F = Σn ( 1 / 2 )**n where n is the term count
n = int(input("Enter no. of terms : "))
i = 1
sum = 0
while i <= n:
    a = (1/2)**i
    sum = float(sum) + a
    i += 1
print("Sum :",sum)