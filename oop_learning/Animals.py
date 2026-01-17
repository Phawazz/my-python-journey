# The classes below will be used to understand duck typing; the other approach besides Inheritance...
# ... used to achieve polymorphism.

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("WOOF!")
        
class Cat(Animal):
    def speak(self):
        print("MEOW!")
        
class Car:
    
    alive = False
    
    def speak(self):
        print("HONK!")
        
