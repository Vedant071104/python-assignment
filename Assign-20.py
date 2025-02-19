# Q.1) write the python script to print first 10 multiple of 5 using range
for i in  range(1,11) :
    print(i*5,end=" ")   
    
# Q.2) write the python script to print first 10 multiple of N
n=int(input("enter the number"))
for i in range(1,11):
    print(i*n,end=" ")
    
# Q.3) write the python script to print first m multiple of N.
n=int(input("enter the number"))
m=int(input("enter the number of multiple of you have"))
for i in range(1,m+1):
    print(i*n,end=" ")
    
# Q.4) write the python script to print the first 10 multiple of n in reverse order
n=int(input("enter the number"))
for i in range(10,0,-1):
    print(i*n,end=" ")
    
# Q.5) write the python script to print table of user choice.
n=int(input("enter the table of your choice"))
for i in range(1,11):
  print("%d x %d= %d"%(n,i,n*i))