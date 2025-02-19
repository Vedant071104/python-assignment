#write the python script to calculate the factorial of given n number. 
n=int(input("enter the number"))
if n>=0:
    s=1
    for e in range(1,n+1):
     s=s*e
    print("sum is:-",s,end=" ")
else:
     print("invalid value")    
