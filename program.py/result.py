


#Q.1) wriet the program to print result with grade.
#Ans-
mark=int(input("enter the mark of student out off 100"))
if 90<mark<=100:
    print("grade is A")
elif 80<mark>=90:
    print("grade is B")
elif 70<mark>=80:
    print("grade is C")
elif 60<mark>=70:
    print("grade is D")
elif 50<mark>=60:
    print("grade is E")
else:
    print("below 50")
    
# Q.2)write the python program to check wether number is positive or negtive
# (using single line if else)
x=int(input("enter any number"))
print("positive" if x>=0 else "negative")
    