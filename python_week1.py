#python lists
#ordered, changeable, allow duplicates
list=["apple","banana","cherry"]
print(list)
list.append("orange")
print(list)
print(len(list))
list.remove("banana")
print(list)
print(type(list))
list.sort()
print(list)

#python tuples
#ordered, unchangeable, no duplicates
tuple=("apple","banana","cherry")
print(tuple)
print(len(tuple))
print(type(tuple))

#python dictionaries
#unordered, changeable, no duplicates
dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}
print(dict)
print(dict["brand"])
dict={
    "brand":"ford",
    "model":"mustang",
    "year":1964,
    "year":1950,
    "color":("red","white","blue")
}
print(dict)
print(len(dict))
print(type(dict))

#python sets
#unordered,unchangable, no duplicates
#false & 0 is considered same value 
set={"apple","banana","cherry",False,True,0}
print(set)
print(len(set))
set1={"apple","banana","cherry"}
set2={1,6,5,7,9}
set3={True,False,False}
print(set1)
print(set2)
print(set3)
print(type(set1))

#python strings
#ordered, unchangeable, allow duplicates
string="Hello, World!"
print(string)
print(len(string))
print("My name is Advika")
a="hello"
print(a)
b="these are fuits"
print(b[1])
#loop through string
for x in "banana":
    print(x)
    
print(len(a))
#check 
txt="The best things in life are free!"
print("free" in txt)
print("expensive" not in txt)

#python conditions and if statements
#a==b , a!=b, a>b, a<b, a>=b, a<=b
a=330
b=200
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
    
z=40
y=40
print("z is greater" if z > y else ("z and y are equal" if z == y else "y is greater"))

s=200
q=33
r=200
if s > q and r> q:
    print("Both conditions are true")
if s>q or q>r:
    print("At least one condition is true")
    
d=33
f=300
if d > f:
    pass  # Do nothing

#python loops
#while loop 
#i=1
#while i < 6:
#    print(i)
#    if i==3:
#        break

k=0
while k<6:
    k +=1
    if k == 3:
        continue    
    print(k)
    
#for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#python Try Except
try:
    print(n)
except:
    print("An exception occurred, n is not defined")
    
try:
    print(m)
except NameError:
    print("Variable m is not defined")
except:
    print("Something else went wrong")
    
    
try:
    print("Hello")
except:
    print("An error occurred")
else:
    print("No errors occurred")
finally:
    print("This will always execute, regardless of an error")
    
#raise an exception
#x = -1
#if x < 0:
#    raise Exception("Sorry, no numbers below zero")  

#python functions
def student(fname, lname):
    print(fname + " " + lname)

student("Emil","anderson")

