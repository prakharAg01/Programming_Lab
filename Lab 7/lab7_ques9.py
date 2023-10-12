S = str(input())
low = S.lower()
A = "abcdefghijklmnopqrstuvwxyz"
count = 0
for i in A:
    if i in low:
        count += 1 
print(count)
if count >= 26:
    print("Panagram")
else:
    print("not panagram")

