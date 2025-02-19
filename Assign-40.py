#Q.1)write the python recurtion  function  to calculate sum of digit of a given number.
def sumOFdigit(n):
    if n!=0:
     return n%10+sumOFdigit(n//10)
    return 0
print(sumOFdigit(2841))
#Q.2)write the python recurtion  function  to calculate sum of factorial of N given number.
def printNfactorial(n):
    if n==0:
        return 1
    return n*printNfactorial(n-1)

#Q.3) write the python recurtion  function  to print binary of a given decimal number.
def decimalTObinary(n):
    if n>0:
        decimalTObinary(n//2)
    print(n%2)
print(decimalTObinary(1))