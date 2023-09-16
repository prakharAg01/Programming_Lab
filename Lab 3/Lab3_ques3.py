#To check if three numbers form sides of a triangle
S1 = float(input("Enter length of a side : "))
S2 = float(input("Enter length of another side : "))
S3 = float(input("Enter length of another side : "))
if (S1+S2) > S3 :
    print("They form a triangle.")
else:
    print("They do not form a triangle.")