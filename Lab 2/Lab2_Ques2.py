#input length and width in feet and calculate area in sq metres
#User input values
L = float(input("Enter Length (in feet) : "))
W = float(input("Enter width (in feet) : "))

l = L * 0.3048
w = W * 0.3048

#calculation
Area = l*w

#Output
print("Area of plot (in meter square) is :",Area)