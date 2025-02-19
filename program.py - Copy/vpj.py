class Employee:
    def putdata(self):
        self.id = int(input("Enter your id: "))
        self.name = input("Enter your name: ")
        self.salary = float(input("Enter your salary: "))

    def display(self):
        print("Employee ID:", self.id)
        print("Employee Name:", self.name)
        print("Employee Salary:", self.salary)

# Creating an instance of Employee and using its methods
a = Employee()
a.putdata()
a.display()
