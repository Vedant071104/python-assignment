#Q.1) write the recursive function to print first n natural number.
def printN(n):
    if n>0:
        printN(n-1)
        print(n)
        
#Q.2) write the recursive function to print revers n natural number,
def printNreverses(n):
    if n>0:
        print(n)
        printNreverses(n-1)
        
#Q.3) write the recursive function to print n odd number.
def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(n*2-1)
        
#Q.4) write the recursive function to print reverse n odd number.
def printNoddreverse(n):
    if n>0:
        print(2*n-1)
        printNoddreverse(n-1)
        
#Q.5) write the recursive function to print MysirG N times.
def printMysirG(n):
    if n>0:
        print("mysirG")
        printMysirG(n-1)

        