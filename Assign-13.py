# Q.1)write the python program to check weather given number is three digit number or not.
x=eval(input("enter any number"))
if 99<x>1000:
    print("Number is three digit")
else:
    print("Number is not the three digit")





# Q.2) write the python script to check weather number is positive, negative or zero.
x=eval(input("enter any number"))
if x>0:
    print("num is positive")
elif x<0:
    print("num is negative")
else:
    print("num is zero")
    
#Q.3) 
a=eval(input("enter  value of a"))
b=eval(input("enter  value of b"))
c=eval(input("enter  value of c"))
d=b**2-4*a*c
if d>0:
    print("real and distinct root")
elif d<0:
    print("imaginary")
else:
    print("real and equal root")
    
    
# Q.4) write the python script t check weather given year is leap year or not.
year=eval(input("enter the year"))
if year%400:
    print(" not leap year")
else:
    print(" leap year ")
    
    
# Q.5)write the python script to find out the greater number omoung three nnumber.
a=eval(input("enter any number"))
b=eval(input("enter any number"))
c=eval(input("enter any number"))
if a>=b and a>=c:
    print("greater number is:","a")
elif b>c:
    print("greater number is:","b")
else:
    print("greater number is:","c")