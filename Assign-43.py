# Q.1) write the python script to find number of vowel in each of the string in a given list of string.Use map function.
"""def vowelcount(n):
    count=0
    for ch in n:
         if ch in "aeiouAEIOU":
             count+=1
    return count
def f1():
    l1=["kanpur","bhopal","mumbai","jaipur"]
    for k in map(vowelcount,l1):
    # print(k)"""
    
# Q.2)
"""def countNumber(v):
    count=0
    while v:
        v=v//10
        count+=1
        return count

    t=(1,234,456,12345,543,2546) 
    for m in map(countNumber,t):
        #print(m)"""
        
# Q.3) 
from functools import reduce


def f3():
    s1={12,45,67,13,54,34}
    x=int(input("enter the number"))
    print(list(filter(lambda n: n if n>x else None ,s1)))
    
 #Q.4)
def f6():
    l1=["2j+3",3.55,"2k+5J",6,23,56]
    print(list(filter(lambda n: n if type(n)==int else None ,l1)))  
 
f6()   

# Q.5) 
def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            h-=1
def f5():
    l1=[200,160,150,90]
    print(reduce(hcf,l1))
f5()
print()
    

        
