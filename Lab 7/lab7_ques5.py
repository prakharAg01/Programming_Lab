#ques5 -- to check various 
S = str(input())
alpha_count = 0
dig_count = 0
low_count = 0
up_count = 0
spec_char = 0
for i in S:
    if i.isalpha():
        alpha_count += 1
        if i.islower():
            low_count += 1
        elif i.isupper():
            up_count += 1 
    elif i.isdigit():
        dig_count += 1
    else:
        spec_char += 1
   
print("alphabets :",alpha_count)
print("Digits :",dig_count)
print("Lowercase :",low_count)
print("Uppercase :",up_count)
print("Special Characters :",spec_char)
