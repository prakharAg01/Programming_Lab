#yo check if second integer is divisible by first integer
X = int(input("Enter a number : "))
Y = int(input("Enter another number : "))

if X < 0 and Y < 0:
    print("Invalid Inputs")
else:
    if Y % X == 0:
        print("Divisible")