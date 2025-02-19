
# Q.1) write the python script to checke weather given number is three digit or not.
x=eval(input("enter any number:-"))
match 1000>x>99:
    case True:
        print("number is three digit")
    case False:
        print("not three digit")

# Q.2) write the python script to check weather number is positive, negative or zero using match.
num=eval(input("enter any number:-"))
match num:
    case num if num>0:
        print("num is positive")
    case num if num<0:
        print("num is negative")
    case _:
        print("num is zero")
        
# Q.3) 
print("1. odd even number")
print("2.positive and non-positive")
print("3.simple interest")
print("4.root and quadratic equation")
choise=int(input("Enter your choice"))
match choise:
    case 1:
        num=int(input("enter any number"))
        if num%2:
            print("number is even")
        else:
            print("numbe is odd")
    case 2:
        num=int(input("enter any number"))
        if num>=0:
            print("number is positive")
        else:
            print("number is negative")
    case 3:
        p=int(input("enter principal amoun:-t"))
        r=int(input("enter rate of interest:-"))
        t=int(input("enter the time in year:-"))
        si=p*r*t/100
        print("simple interest is:-",si)
    case 4:
        a=int(input("enter value of a="))
        b=int(input("enter value of b="))
        c=int(input("enter value of c="))
        r1=(-b+(b**2-4*a*c)**0.5)/2*a
        r2=(-b-(b**2-4*a*c)**0.5)/2*a
        print("root are",r1,"and",r2)
    
        
# Q.4) 
data=eval(input("enter the any data"))
match data:
    case data if(int):
        print("monday")
    case data if(float):
        print("tuesday")
    case data if("complex"):
        print("wednesday")
    case data if("bool"):
        print("thursday")
        
# Q.5) 
str=input("enter the string")
match str:
    case str if str in "MysirG":
        print("1")
    case str if str in "education":
        print("2")
    case str if str in "services":
        print("3")
        
    
    
    