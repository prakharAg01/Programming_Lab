#to display the tables of all the numbers from 1 to N
#input
N = int(input())
i = 1     #initiate i

while i <= N:    #condition 1
    j = 1  #initiate 2
    while j <= 20:   #condition 2
        print(i, "x", j, "=", i * j)   #output
        j += 1    #loop 2
    i += 1     #loop 1