#Without inbuilt func
S = str(input("Enter a sentence : "))
word = str(input("Enter a word : "))
count = 0 
for i in S.split():
    if i == word:
        count = count + 1
print(count)

#with inbuilt function
S = str(input("Enter a sentence : "))
word = str(input("Enter a word : "))
print(S.count(word))
