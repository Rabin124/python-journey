# Base class
class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

# First-level derived class
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

# Creating instances of ToyotaCar
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.brand)  # Output: fortuner
print(car2.brand)  # Output: prius

# Second-level derived class
class Fortuner(ToyotaCar):
    def __init__(self, brand, type):
        super().__init__(brand)  # Call parent constructor to set brand
        self.type = type         # Set Fortuner-specific attribute

# Creating instance of Fortuner
car3 = Fortuner("fortuner", "SUV")
car3.start()  # Output: Car started

# Optional: print brand and type
print(car3.brand)  # Output: fortuner
print(car3.type)   # Output: SUV



class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A, B):
    varC = "welcome to class C"

c1 = C()
print(c1.varA)  # Output: welcome to class A
print(c1.varB)  # Output: welcome to class B
print(c1.varC)  # Output: welcome to class C
