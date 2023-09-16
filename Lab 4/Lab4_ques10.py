#quadratic equation
print("Ax^2 + Bx + c = 0")
A = int(input("Enter value of A : "))
B = int(input("Enter value of B : "))
C = int(input("Enter value of C : "))
if A != 0:
    D = B**2 - 4*A*C
    if D == 0 :
        print("Real & equal roots.")
        R = -B/(2*A)
        print("Solution is :",R)
    elif D > 0:
        print("Real, unequal roots/solutions.")
        R1 = (-B + (D)**(1/2))/(2*A)
        R2 = (-B - (D)**(1/2))/(2*A)
        print("Solutions are :",R1, R2)
    else:
        print("Complex Roots")
else:
    print("Invalid Inputs")