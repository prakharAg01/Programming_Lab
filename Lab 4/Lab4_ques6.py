#to find if a number is a palindrome or not
N = int(input("Enter a number : "))
if N<0:
    print("invalid")
else:
    X = N
    reverse = 0
    while N > 0:
        temp = N%10
        reverse = reverse*10 + temp
        N = N//10
    if reverse == X:
        print("It is a palindrome")
    else:
        print("It is not a palindrome.")