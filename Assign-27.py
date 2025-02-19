#write the python script to print string in reverse order.
a=input("inter the string")
print(" ".join(a.split(" ")[::-1]))

#write the python script to extract number from given text and store all the number 
# in a list.
num=[]
s1=input("enter any text")
# s1=we have three digit 4,5 and 6
for word in s1.split(" "):
    for w in word.split(","):
        if w.isdigit():
            num.append(int(w))
            print(num,end=(" "))
            
#write the pyhon script to print the palindrom number 
s2=input("enter the number")
if s2[::-1]==s2:
    print("palindrome number")
else:
    print(" Not a palindrome number")
    
#write the python script to tranform given string into uppercase.
s2=input("enter the number")
print(s2.upper())

# Write the python script to print maximum lenth word from given string.
s2=input("enter the number")
l1=[len(w) for w in s2.split(" ")]
print(s2.split(" ")[l1.index(max(l1))])
