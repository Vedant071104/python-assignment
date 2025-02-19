# Q>1) write the python recursive function to print N even number.
def printNeven(n):
    if n>0:
        printNeven(n-1)
        print(2*n)
        
#Q.2) write the python recursive function to print Neven number in reverse order.
def printNevenreverse(n):
    if n>0:
        print(n*2)
        printNevenreverse(n-1)
        
# Q.3) write the python recursive  function to print square of first n natural number.
def printNsquare(n):
    if n>0:
        printNsquare(n-1)
        print(n**2)
        
# Q.4) write the python recursive function to print cube of first N natural.
def printNcube(n):
    if n>0:
        printNcube(n-1)
        print(n**3)
        

# Q.5) write the python recursive function to print reverse of given number.
def rev(n):
    if n!=0:
        print(n%10)
        rev(n//10)
    