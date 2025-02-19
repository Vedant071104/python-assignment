# Q.1) write the python program to find out number is negative or positive

x=int(input("enter any number"))
if x>=0:
    print("number is positive")
else:
    print("number is negative")
    
# Q.2) write the python program to checke wether the given number is divisible by 5 or not.
x=int(input("enter any number"))
if x%5==0:
    print("num is divisible by 5")
else:
    print("num not divisible by 5")

# Q.3) write the python script to check weather  given number is even or odd.
x=int(input("enter any number"))
if x%2==0:
    print("number is even")
else:
    print("number is odd")
    
# Q.4) write the python script print to print greater between two number. 
# print only once evev if the number are the same.
x=int(input("enter first number"))
y=int(input("enter second number"))        
if x>y:
    print("greater number is:",x)
else:
    print("greater number is:",y)
    
# Q.5)write the python script print to print two given word in dictionary order.
s1=input("enter first word:")
s2=input("enter second word:")
if s1<s2:
    print(s1,s2)
else:
    print(s2,s1)

