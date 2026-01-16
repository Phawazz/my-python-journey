# All classes moved here in order to get things organized.
# # They will be imported into the file being worked on.

class  Car:
    def __init__(self, model, year, color, for_sale): # dunder method (double underscore)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
    def drive(self):
        print(f"You drive the {self.color} {self.model}")
        
    def stop(self):
        print(f"You stop the {self.color} {self.model}")
        
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
        
        
class Student: 
    
    class_year = 2024 # a class variable.
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
        
class Animal: # Parent class for Dog, Cat, and Mouse
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is asleep")
        
        
        
class Dog(Animal): 
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

class Organism: # More like a grandparent
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Organism):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Organism):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # a typical example of multiple inheritance; the child class (Fish) inheriting from more than one parent
    pass

# Abstract classes in python
from abc import ABC, abstractmethod
class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass
    
class Bus(Vehicle):
    
    def go (self):
        print("You drive the bus")
        
    def stop(self):
        print("You stop the bus")
        
        
class Motorcycle(Vehicle):
    
    def go(self):
        print("You ride the motorcycle")
    
    def stop(self):
        print("You stop the motorcycle")
        
class Boat(Vehicle):

    def go(self):
        print("You sail the boat")
    
    def stop(self):
        print("You anchor the boat")
        
        
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius }")
        
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height