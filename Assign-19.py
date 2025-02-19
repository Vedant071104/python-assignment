# Q.1) write the python script to print each character of string with its corresponding unicode.
str=(input("enter the string"))
for i in str:
    print(i,ord(i),sep="-",end=" ")
    
# Q.2)write the python script to print only vowels of the give string.
n=(input("enter the string"))
for i in n:
    if i in "aeiouAEIOU":
     print(i,end=" ")
    
# Q.3) write the python script to count occurrence of spaces in given string.
n=(input("enter the string"))
count=0
for x in n:
    if x==" ":
        count+=1
        print("Total space:=",count)
        
# Q.4)write the python script to print unique digit of a given integer.
n=int(input("enter the number"))
for digit in "0123456789":
    if digit in str(n):
        print(digit,end=" ")
        
# Q.5)write the python script to count number of digit in a given number.
n=int(input("enter the digit:="))
count=0
for x in str(n):
    count+=1
    print("number of digit:-",count)
    
