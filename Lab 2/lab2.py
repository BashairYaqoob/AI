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

s=student()
s.display1()
#---------------------------
