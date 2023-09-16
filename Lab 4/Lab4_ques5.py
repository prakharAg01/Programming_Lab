#to find factorial of a number
N= int(input("Enter a number : "))
i = 1
fact = 1
if N == 1:
    print("fact =",1)
elif N <=0:
    print("Invalid input")
else:
    while i <= N:
        fact = fact*i
        i = i+1
    print("factorial =",fact)
