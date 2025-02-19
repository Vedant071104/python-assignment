# Q.1) define a python class person with instance object variable name and age. set instance object variable
#      in __init__() method. also define show method t odisplay name and age of person.

class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print("name is:-",self.name)
        print("age is:-",self.age)
        
a=person("vedant",20)
a.show()

# Q.2) define a class circle with instance object variable radius provid a setter and getter
# for radius also define getArea() and getcircumference() method.
 
class circle:
    def __init__(self,r):
        self.radius=r
    def setradius(self):
        self.radius=a
    def getradius(self):
        return self.radius
    def getarea(self):
        return 3.14*a**2
    def getcircumference(self):
        return 2*3.14*a**2

# Q.3) define a class Rectangle with length and breath as instance object variable.
#      provide setDimention(),showDimention() and getArea() method in it .
class rectangel:
    def __init__(self,l,b):
        self.length=l
        self.breath=b
    def setDimention(self):
        self.length
        self.breath
    def showDimention(self):
        print("length:-",self.length,"breath:-",self.breath)
    def getarea(self):
        return self.length*self.breath
    
# Q.4) Define class book with instance object variable booked, title and price
# initialise them via__init__() method. also define method to show book variable.
class book:
    def __init__(self,id,t,p):
        self.bookid=id
        self.title=t
        self.price=p
    def show(self):
        print("BOOK ID:-",self.bookid  ,"BOOK TITAL:-",self.title  ,"BOOK PRICE:-",self.price,end="")
        
obj2=book(123,"atomic habit",1200)
obj2.show()

# Q.5) Define a class team with instance object variable a list of team member name provide 
#     method to input member name and display member names.
class Team:
    def __init__(self):
        self.TeamMemberName=[]
    def inputmember(self):
        print("enter team member names eperated by comma:-")
        self.TeamMemberName=input().split(",")
    def showMembername(self):
        for name in self.TeamMemberName:
            print(name)
obj3= Team()
obj3.inputmember()
obj3.showMembername()