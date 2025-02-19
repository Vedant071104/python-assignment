# Write the python function to check if give function is even.
def iseven(n):
    n%2==0
    return n
x=iseven(3)
print("even:-",x)
#               AND
def iseven(n):
    return n%2==0

# Write the python function to find greater among three number(TSRS)
def greater(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
y=greater(500,1000,1500)
print("greater number is:-",y)

# Write python function to check weather number is prime.(TSRS)
def isprime(n):
    for i in range(2,n):
        i%n==0
        return False
    return True
# Q.4) Write the python function to cheak if an year is leap year(TSRS)
def isLeaPyear(year):
    return year%400==0 if year%100==0 else year%4==0 


#Q.5) Write the python function ti calculate factorial of number.(TSRS)

def Factorial(n):
    f=1
    for i in range(1,n+1):
     f=f*i  
    return f