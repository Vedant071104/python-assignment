 # write the python script to calculate sum of element of the list.
l1=[ int(e) for e in input("enter the number in list which is seperated by comma").split(",")]
print("sum is",sum(l1))

#write the python script to find the average of elment of list.
l2=[int(v) for v in input("enter the number in list which is seperated by comma").split(",")]
print("average is:-",sum(l2)/len(l2))

#write the python script to create the list of square of number of given list.
l1=[int(i) for i in input("enter the element seperated bt comma").split(",")]
l2=[e**2 for e in l1]
print(l2)

#write the python script to sort the list element in desending order.
l1=[int(e) for e in input("enter the element seperated by comma").split(",")]
l1.sort(reverse=True)
print(l1)

#write the pyhon script to print only even places of list.
l1=[int(j) for j in input("enter the element seperated bt comma").split(",")]
l2=l1[1::2]
print(l2)