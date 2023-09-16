#To display temperature in F while taking input in Celcius
temp = float(input("Enter temperature in Celsius : "))  # user input
F = temp*(9/5) + 32  # calculation 
print("Temperature in Fahrenheit is ",F) # output
K = temp+273
print("Temperature in Kelvin is ",K)