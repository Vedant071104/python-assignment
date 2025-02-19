
# write the  python function to print first N odd natural number.(TSRS)
def oddnum(n):
    for i in range(1,n+1):
       print(i*2-1)
       
   # write python function to print 
def printNprime(n):
    x=2
    while n:
     if isprime(x):
         print(x,end=" ")
         n-=1
         x+=1
        
#Q.3) write the python function to print prime number between between two number.
def printprimebetween(a,b):
    for x in range(a+1,b):
      if isprime(x):
          print(x,end=" ")
           
#Q.4)print nfibonici function .

def printNfb(n):
    a,b=-1,1
    while n:
        c=a+b
        print(c,end=" ")
        a,b=b,a
        n-=1
        
#Q.5) writer the python function to print all factorial of given number.
def printNfactorial(n):
    for i in range(1,n+1):
        if  n%i==0:
            print(i,end=" ")
