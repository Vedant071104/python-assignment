# Q.1) write the python program to find out number is negative or positive

x=int(input("enter any number"))
if x>=0:
    print("number is positive")
else:
    print("number is negative")
    
#Q.1)number without last digit
a=int(input("enter any number"))
print("number without last digit",a//10)

# Q.2)number with last digit.
a=int(input("enter any number"))
print("number with last digit",a%10)

#Q.3) write the program to swap data of two variable.
a=20
b=30
a,b=b,a
print(a,b)
# second method (used in c++)
A=1
B=2
temp=A
A=B
B=temp
print(A,B)
# Q.4) enter number with first digit.
a=int(input("enter any number"))
print("number with first digit",a//100)

# Q.5)write the program to enter the middle number of three digit

a=int(input("enter any three digit number"))
print("number with middle digit",a//10%10)




    