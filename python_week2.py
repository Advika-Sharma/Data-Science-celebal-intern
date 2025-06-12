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