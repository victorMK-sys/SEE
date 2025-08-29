# Assignment 1: 
class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age

  def sayHello(self):
    print(f"Hello.My name is {self._name} and I am {self._age} years old.")

person1 = Person("Garfield", 54)

person1.sayHello()

# Assignment 2:
class Animals:
  pass

class Lion:
  def makeSound():
    print("Roar!!")
  
class Pig:
  def makeSound():
    print("Grunt")

Lion.makeSound()
Pig.makeSound()