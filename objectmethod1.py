class Student:
    college = "Green Valley"
    def __init__(self, fullName, rollno):  
        self.name = fullName
        self.rollno = rollno
    def welcome(self):
        print("Welcome to the class,", self.name)

    def get_rollno(self):
        return self.rollno

s1 =Student("Sai Pallavi", 10)
s1.welcome()
print(s1.get_rollno())
