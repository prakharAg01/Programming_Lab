#to check if the input number is a palindrome 
n = int(input("Enter a 5 digit  number : "))   #user input
#initiating two temporary variables
one = n
two = 0
#process to break number into digits
while n > 0 :
    dig = n%10
    two = two*10 + dig
    n = n//10
#condition for palindrome
if one == two :
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")