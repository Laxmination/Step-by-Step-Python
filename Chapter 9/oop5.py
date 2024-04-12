# inheritance example
class Car: # Parent class
    color = "Royal Blue"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class FarariCar(Car): # Child class
    def __init__(self, name):
        self.name = name

car1 = FarariCar("Fortuner")
car2 = FarariCar("Prius")

print(car1.start())
print(car2.color)
