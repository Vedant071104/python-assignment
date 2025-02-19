 #write the python script to check if the given string has only alphabet in it.
v=input("enter string only")
l1=",".join([chr(e) for e in range(97,123)])
l2=",".join([chr(e) for e in range(65,91)])
l=l1+l2
for e in v:
    if e not in l:
        print("string has not character value")
        break 
    else:
        print("string has only character value in it")
        

 #write the python script to check if the given character is present in given string.
s=input("enter required cheracter ")
v1=",".join([chr(i) for i in range(97,123)])
v2=",".join([chr(i) for i in range(97,123)])
v=v1+v2
for i in s:
    if i not in v:
        print("requird character are not present in it")
        break
    else:
        print("required charecter present in it")
#                      or
c=input("enter the string ")
ch=input("enter the required charater")
for e in c:
    if ch in e:
        print(ch, "is in",c)
    else:
        print(ch,"is not in",c)
        
#write the pyhon script to count the vowels in given string.
z=input("enter the string")
i=("aeiouAEIOU")
count=0
for e in z:
    if e in i:
        count+=1
        print("count is-:",count,end=",")
        
#write the python script to count the word in a given string.
s1=("enter the string")
print("count of word is:-",len(s1.split(" ")))

#write the pytho script to severse the string.
s=input("enter the string")    
",".join(s.split(' ')[::-1])