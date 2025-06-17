#imporing modules
def greeting(name):
    print("Hello, " + name)
    
person1 = {
    "name": "Advika",
    "age": 21,
    "country": "India"
}
    
import mymodule
mymodule.greeting("Advika")

import mymodule as mx
a=mx.person1["name"]
print(a)
a = mx.person1["age"]
print(a)

#built in modules
import platform
x=platform.system()
print(x)

y=dir(platform)
print(y)