class Person:
    __name = "anonymous"

    def __hello(self): #private method
        print("Hello Customer")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome()) # Npw this can be accessed
print(p1.__hello()) # this method cannot be accessed by this object