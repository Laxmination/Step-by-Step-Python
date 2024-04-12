# Define an Employee class with attributes role, department and salary. this class also has a showDetail() method.
# Create an Engineer class that inherits properties from Employee and has additional attributes :name and age.



class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetail(self):
        print("role =", self.role)
        print("Department =", self.department)
        print("Salary =", self.salary) 


class Engineer(Employee):
    def __init__(self, Name, age):
        self.name = Name
        self.age = age
        super().__init__("Engineer", "IT", "60,000" )


e1 = Employee("Manager", "B-bing", "80,000")
e1.showDetail()

e2 = Engineer("Supriya Shrestha", 30)
print(e2.name)
print(e2.age)
e2.showDetail()