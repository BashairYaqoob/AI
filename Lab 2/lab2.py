variable length argument:
def varlength(*a):
    for x in a:
        print(x, "->", type(x))

varlength(2.4)
varlength('Yogs')
#output:
#2.4 -> <class 'float'>
#Yogs -> <class 'str'>

class abc:
    def sumall(self, *args):
        return sum(args)
    
a=abc()
print(a.sumall(1,2))
print(a.sumall(1,2,3))
print(a.sumall(4.6,2.2))

#architecture of class
class person: 
    pass #future implementation

s= person()
#---------------
class person: 
    x=10
    def display(self):
        print("person")

s= person()
s.display()
print(s.x)
#-------------------
class person: 
    x=10
    def __init__(self, name, age): #instance variable: values can change
        self.name=name
        self.age=age

    def display(self):
        print(f"name is {self.name} and age is {self.age}")

s= person('abc', 5)
s1=person("xyz", '55')
s.display()
s1.display()
print(s.x)
print(s1.x)

#output:
#name is abc and age is 5
#name is xyz and age is 55
#10
#10
#------------------------------
#inheritance
class person: 
    def display(self):
        print("parent method")
class student(person):
    def display1(self):
        print("child method")
        self.display()
class teacher(person, student):
    pass

s=student()
s.display1()
#-----------------------------
#inheritance
class person: 
    def display(self):
        print("parent methode")


class student(person):
    def display(self): #methode override
        print("child methode")
        
    def display1(self):
        self.display() #priority to it's own class ->"childmethode"

s=student()
s.display1()
#-----------------------
#inheritance
class person: 
    def __init__(self):
        self.x=10
    def display(self):
        print("parent methode")


class student(person):
    def __init__(self):
        self.y=20
    def display(self): #methode override
        print("child methode")
        
    def display1(self):
        self.display() #priority to it's own class ->"childmethode"

s=student()
s.display1()
print(s.y)
print(s.x)#error
#----------------------
class person:
    def display(self):
        print("parent methode")


class student(person):
    def display(self):
        print("child methode")
        
    def display1(self):
        super().display() #access parent method
        self.display()
#--------------------------
class person:
    def __init__(self):
        self._x=10 #_ -> protected. accessible within itself and child class
s=student()
s.display1()
#---------------------------
class person:
    def __init__(self):
        self._x=10
    def display(self):
        print(f"parent {self.x}")
class student(person):
    def display1(self):
        print(f"protected {self._x}") #accesing protected attribute

s=student()
s.display1()
#---------------------------
import math
print(math.sqrt(16))
print(math.sin(90))
print(math.cos(0))
print(math.pi)
print(math.pow(2,3))
