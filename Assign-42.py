# Q.1) write the function to receives variable length argument to calculaet average of integer.
# it return  average of number
def cal_avg(*t):
    return sum(t)/len(t)

# Q.2) write the function to receives vaariable length argument to find greatest element.
# to return greatest element.

def greatest_Ele(*t):
    return max(t)

# Q.3) write the function to receives vaariable length argument to filter odd even number.
# store all even number in list and odd number in another list store both list in tupel and return.

def FilterEvenodd(*t):
    even=[]
    odd=[]
    for i in t:
        if i%2==0:
            even.uppend(i)
        else:
            odd.uppend(i)
            return (even,odd)
        
def maxstring(*t):
    l1=[]
    max(len(t.splite(""))).uppend(l1)