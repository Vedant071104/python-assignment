# Q.1) write the python recurtion  function  to calculate sum of N natural number.
def sumN(n):
    if n==1:
        return 1
    return n+sumN(n-1) 

# Q.2)write the python recurtion  function  to calculate sum of N odd number.
def addNodd(n):
    if n==1:
        return 1
    return 2*n-1+addNodd(n-1) 
# Q.3) write the python recurtion  function  to calculate sum of N even numbber.
def addNeven(n):
    if n==1:
        return 1
    return n*2+addNeven(n-1)
# Q.4) write the python recurtion  function  to calculate sum of square of N natural number.
def squareN(n):
    if n==1:
        return 1
    return n**2+squareN(n-1)
# Q.5) write the python recurtion  function  to calculate sum of.
def cubeN(n):
    if n==1:
        return 1
    return n**3+cubeN(n-1)