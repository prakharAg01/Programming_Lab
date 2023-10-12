#ques4 -- To check if a string is palindrome or not (word)
'''S = str(input())
if S == S[::-1]:
    print(S,"is a PALINDROME")
else:
    print(S,"is NOT A PALINDROME")'''


#(sentence)
S = str(input("Enter a sentence : "))
a = S.split(" ")
print(a)
b = a[::-1]
if a == b:
    print("Palindrome")
else:
    print("Not palindrome")