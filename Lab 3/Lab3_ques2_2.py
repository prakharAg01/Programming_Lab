#To calculate BMI (lbs and inches)
#user input
W = float(input("Enter weight (in lbs) : "))
H = float(input("Enter height (in inches) : "))
#using formula
bmi = 703*(W/(H**2))
#output
print("BMI is :",bmi)