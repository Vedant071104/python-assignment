class employee:
    def putdata(self):
        self.id=int(input("Enter tour id"))
        self.name=input("enter your name")
        
        self.salary=float(input("enter your salary"))
    def display(self):
         print("employee id:-",self.id)
         print("employee name:-",self.name)
         print("employee salary:-",self.salary)
a=employee()
a.putdata()
a.display()