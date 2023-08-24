# William Smith
# 2023/08/24
# https://www.linkedin.com/in/williamsmithe/ 
# https://github.com/WilliamSmithEdward
# This project is public domain.
#
# The purpose of this project is to demonstrate programming
# principles and syntax in Python for someone who is generally 
# familiar with programming in another language.

#############
# Hello world
#############
print("Hello World!");

###########
# Variables
###########
x = 5
name = "Will"

############
# Data Types
############
num = 3.14
text = "Hello"
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}

###################
# Conditional logic
###################
if name == "Will":
    print("Hello " + name)
elif name == "Bob":
    print ("Hello " + name)
else:
    print ("Hello \"someone\"")

########################
# For 'i' itterator loop
########################
for i in range(0, 4):
    print("Index: " + str(i))

###############
# For each loop
###############
myNameList = ['Will', 'Bob', 'John']
for name in myNameList:
    print("Your name is: " + name)

############
# While Loop
############
counter = 0
while counter < 4:
    print("Counter: " + str(counter))
    counter += 1

###########
# Functions
###########
def greet(name):
    return "Hello, " + name

message = greet("Will")
print(message)

####################
# Function Overloads
####################
def greet(name, age):
    return "Hello, " + name + ", you are " + str(age) + " years old"

message = greet("Will", 35)
print(message)

##################################
# List Comprehensions / Generators
##################################
squares = [x**2 for x in range(5)]

for number in squares:
    print(str(number))

def square_generator(n):
    for x in range(n):
        yield x**2

squareGen = square_generator(5)

for number in squareGen:
    print(str(number))

################
# Error handling
################
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

###############
# File I/O
###############
with open("myFile.txt", "r") as myFile:
    content = myFile.read()

with open("newFile.txt", "w") as newFile:
    newFile.write("This is some content.")

###################
# Class declaration
###################
class Animal:
    def __init__(self, name):
        self.name = name

    def getType(self):
        return self.name

    def speak(self):
        pass

###############
# Instantiation
###############
animal = Animal("Dog")
print(animal.getType())

#############
# Inheritance
#############
class Dog(Animal):
    def speak(self):
        return self.name + " says 'Woof'!"

class Cat(Animal):
    def speak(self):
        return self.name + " says 'Meow'!"

dog = Dog("Rover")
print(dog.speak())

##############
# Polymorphism
##############
animalList = { Dog("Spike"), Cat("Whiskers") }

for animal in animalList:
    print(animal.speak())

####################
# Lambda Expressions
###################
square = lambda x: x**2
print(square(5))

hello = lambda x: "hello " + x
print (hello("Will"))

#####
# Map
#####
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))

########
# Filter
########
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))

########
# Reduce
########
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

############
# Decorators
############
def myDecorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@myDecorator
def sayHello():
    print("Hello!")

sayHello()

#############
# Async/Await
#############
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(main())

#############
# Parallelism
#############
import multiprocessing

def calculateSquare(number):
    return number ** 2

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculateSquare, numbers)
    
    print("Original Numbers:", numbers)
    print("Squared Numbers:", results)

#############
# Concurrency
#############
import concurrent.futures

def calculateSquare(number):
    return number ** 2

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(calculateSquare, numbers))
    
    print("Original Numbers:", numbers)
    print("Squared Numbers:", results)