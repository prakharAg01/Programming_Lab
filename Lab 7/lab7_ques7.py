#Take a sentence as input and remove all the duplicate characters from the string.
S = str(input("Enter a sentence : "))
A = ""
for i in S:
    if i not in A :
        A = A + i
print(A)