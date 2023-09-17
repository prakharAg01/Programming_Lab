#Take a positive number N as input and display all the numbers that are not divisible by N and lie
#in the range 1 – 1000. Use continue statement with while loop.

N = int(input())
i = 1
while i <= 1000:
    if i%N == 0:
        print(i)         
    i += 1
