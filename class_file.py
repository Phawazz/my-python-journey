# Class moved to a different file simply because they take space. It will be imported into the file being worked on.

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
        
        
        
class Animal:
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
