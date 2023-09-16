#to find the total numbers which are divisible and not divisible by N 
N = int(input())    #input 
count1 = 0
count2 = 0
while True:         #condition 0 start
    X = int(input())    #input of numbers to test
    if X == -999 :      #stop the loop only when -999 is entered
        break
    elif X%N == 0 :     #condition 1 (divisible)
        count1 += 1
    elif X % N != 0:    #condition 2 (not divisible)
        count2 += 1
print("Total numbers which are divisible by",N,":",count1)          #output 1
print("Total numbers which are not divisible by",N,":",count2)      #output 2
    
        
