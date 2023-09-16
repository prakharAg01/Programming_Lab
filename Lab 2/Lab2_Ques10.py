#User input
T = int(input("Enter time in seconds : "))
H = T//3600 # conversion to hours
R = T%3600 #remaining
mins = R//60 #conversion to minutes
secs = R%60 #remaining Seconds
print("Time :", H,"hours",mins,"mins",secs,"secs") #output
