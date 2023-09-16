#to check if a number is prime or not
N = int(input())
i = 2
if N > 1:
    while i < N:
        if N%i == 0:
            print("It is not a Prime number")
            break
        i += 1
    else:
        print("It is a Prime number")
elif N < 1 :
    print("invalid")