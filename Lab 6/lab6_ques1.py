#to count total number of vowels, consonants and words in a sentence
S = str(input("Enter a sentence : "))
vow = ['a','A','e','E','i','I','o','O','u','U']
v_count = 0
con_count = 0 
word_count = 0 
space = 0 
for i in S:
    if i in vow:
        v_count += 1
    elif i != " " and i != "\t":
        con_count += 1
    elif i == " ":
        space += 1
words = space + 1
print("Vowels are :",v_count)
print("Consonants are :",con_count)
print("Total Words are :",words)
