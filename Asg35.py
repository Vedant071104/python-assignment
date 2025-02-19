#Q.1)
def printNLCM(a,b):
    L=a if a>b else b
    while L<a*b:
        L%a==0 and L%b==a
        return L
    L+=1
    
#Q.2)write the python function to count words in given string.
def countword(text):
    return len(text.split(" "))
#Q.3)write the python function to print prime number between a,b.
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True

def printprimeN(a,b):
 return[ x for x in range(a+1,b) if isprime(x)]

#Q.3) write 
def isprime(n):
   for i in range(2,n):
       if n%i==0:
           return False
       return True
def printprimebetween(a,b):
    return[x for x in range(a+1,b) if isprime(x)]
#Q.4)
def Fiiter_Text(Text):
    wordlist=Text.split(" ")
    d1=dict()
    for chcode in range(97,123):
       d1[chr(chcode)]=[]
       for word in wordlist:
           d1[word[0]].append(word) 
           return d1
#Q.5) 
def Commonfactorial(a,b):
    comfactor=[]
    v=a if a<b else b
    for f in range(1,v+1):
       if a%f==0 and b%f==0:
           comfactor.append()
    return tuple(comfactor) 
#