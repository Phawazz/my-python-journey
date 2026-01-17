from class_file import Car
        
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

print(car1) # this returns the memory address only

print(car2.model) # . is the attribute access operator
print(car2.year)
print(car2.color)
print(car2.for_sale)

car1.drive()
car1.stop()
car2.describe()

# Class variables
from class_file import Student
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(student1) # returns the memory address only as well

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

print()
print(Student.class_year) # it's good practice to access a class variable by the class itself rather than via any instance from the class.

# Inheritance in python: multilevel vs multiple.
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
from class_file import Organism, Prey, Predator, Rabbit, Hawk, Fish

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt()
fish.flee()

hawk.eat()
fish.sleep()
hawk.hunt()

# # Abstract classes in python

from class_file import Vehicle, Bus, Motorcycle, Boat

"""
vehicle = Vehicle()
This returns the error 'Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop''
That simply explains the fact that we can't create objects directly from an abstract class, rather, they have to first be subclassed.
"""

bus = Bus()
bus.go()
bus.stop()

motorcycle = Motorcycle()
boat = Boat()

boat.go()
boat.stop()

motorcycle.go()
motorcycle.stop()

# ---
from class_file import Shape, Circle, Square, Triangle

circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=6)
triangle = Triangle(color="yellow", is_filled=True, width=7, height=8)

print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

triangle.describe()

# ---
from Shapes import Shape, Circle, Square, Triangle, Pizza

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperonni", 15)]
print(shapes) 

for shape in shapes:
    print(f"{shape.area()}cm^2")
    
# Duck Typing in Python
from Animals import Animal, Dog, Cat, Car

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)