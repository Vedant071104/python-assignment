# write the python script to creat tuple from given list.
l1=[20,30,40,50]
t1=tuple(l1)
print(t1)

#write the python script to rever the tuple.
t1=(10,20,30,40,50)
print(t1[::-1])

# write the python scriptto create the list of tuple where each tuple is a pair of 
# pair of element, first element if uppercase and second element is ti's unicode.
l1=[]
for e in range(65,91):
    l1.append((chr(e),e))
    print(l1)

#write the python script to find the sum of all odd number stord in tuple.
t1=(10,45,62,22,30,67)
print("sum is", sum([e for e in t1 if e%2]))