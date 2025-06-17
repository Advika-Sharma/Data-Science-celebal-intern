#python classes/Objects

class myclass:
    x=5
    
p1=myclass()
print(p1.x)

#python init function 
#Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#python str function 
#The __str__() function controls what should be returned when the object is represented as a string.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

#python object 
#The __object__() function is used to return a string representation of the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
print(p1) 

del p1.age
del p1

class Person:
    pass

#python inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()
#creating a child class
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#creating a child class with init function
def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()

#using the super() function
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#python add properties to child class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.printname()
x.welcome()

#python encapsulation
#refers to the bundling of data (attributes) and methods (functions),
# that operate on the data into a single unit, typically a class.

#public attributes
class Public:
    def __init__(self):
        self.name = "John"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible

#protected attributes
class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()

#private attributes
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError

#python opeaning and reading files
#File Handling
#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#There are four different methods (modes) for opening a file:
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#
#"x" - Create - Creates the specified file, returns an error if the file exists
#In addition you can specify if the file should be handled as binary or text mode
#
#"t" - Text - Default value. Text mode
#
#"b" - Binary - Binary mode (e.g. images)

f=open("demofile.txt")
print(f.read())
f.close()

#or
with open("demofile.txt") as f:
  print(f.read(5))
  print(f.readline())
  print(f.readline())
  
#looping
with open("demofile.txt") as f:
  for x in f:
    print(x)

#write to file
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())
  
#overwrite the file
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())
  
#delete a file
import os
os.remove("demofile.txt")

  