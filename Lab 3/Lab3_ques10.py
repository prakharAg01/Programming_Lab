#to find the largest of 3 numbers using nested if else condition.
#user input
N1 = int(input())
N2 = int(input())
N3 = int(input())
#applying conditions along with outputs
if N1 > N2 :
    if N1 > N3 :
        print(N1,"is largest among the three.")
    else:
        print(N3,"is largest among the three.")
elif N2 > N1 :
    if N2 > N3 :
        print(N2,"is largest among the three.")
    else:
        print(N3,"is largest among the three.") 
else:
    print(N3,"is largest among the three.")