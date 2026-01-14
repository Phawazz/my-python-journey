from class_file import Car
        
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1) # this returns the memory address only

print(car1.model) # . is the attribute access operator
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car1.stop()
car2.describe()

# Class variables
from class_file import Student
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

print()
print(Student.class_year) # it's good practice to access a class variable by the class itself and not any instance from the class.

# Inheritance in python
from class_file import Animal, Dog, Cat, Mouse

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()

# Multiple and multilevel inheritance in python
from class_file import Prey, Predator, Rabbit, Hawk, Fish

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt()
fish.flee()

hawk.eat()
fish.sleep()
hawk.hunt()

# Abstract classes in python
class Vehicle:
    pass