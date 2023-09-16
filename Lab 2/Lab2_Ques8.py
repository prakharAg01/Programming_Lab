#To check if an year is a leap year or not

year = int(input("Enter year : ")) # user input

if year > 0:  # conditions
    if year % 100 == 0:
        if year % 400 == 0:
            print("LEAP YEAR")
    elif year % 4 == 0:
        print("LEAP YEAR")
    else:
        print("Not Leap Year")