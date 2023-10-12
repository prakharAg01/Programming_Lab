#ques2
# --- 1 --- Prints total characters other than space
S = str(input("Enter a sentence : "))
sum = 0
for i in S:
    if i != " ":
        sum = sum + 1
print("Length of string :",sum)

# --- 2 --- Prints total string length
S = str(input())
sum = 0
for i in S:
    sum += 1
print(sum)