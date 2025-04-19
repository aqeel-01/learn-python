

# del keyword
'''
used to delete object properties or object itself


del s1.name

del s1
'''

'''
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Ali")

print(s1)
print(s1.name)

del s1
print(s1.name) # it will throw error b/c now s1 object didn't exist

'''
# private(like) attributes & methods
'''
conceptual implementations in python

private attributes & methods are meant to be used only within the class and are not
accesibile from the outside the class

# private like  , not exactly as used in c++ or java

'''
'''
class Account:

    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass

acc1 = Account("123456","xyz")
print(acc1.acc_no)
print(acc1.acc_pass) # it's generally no  good practice , to expose such a information

'''
# so solution , use public or private  concept in clases 

'''
class Account:

    def __init__(self , acc_no , acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # infront of object name use double underscore __

    def reset_pass(self):
        print(self.__acc_pass)
    


acc1 = Account("123456","xyz")
print(acc1.acc_no)
#print(acc1.__acc_pass) #error
#print(acc1.__acc_pass)  # error b/c it's private now

print(acc1.reset_pass())


'''

'''

class Person:

    __name = "anonymous"


    def __hello(self):
        print("hello person! ")

    def welcome(self):
        self.__hello()
    
p1 = Person()
#print(p1.__name)
print(p1.welcome())

'''

# Inheritance

'''
when one class (child / derived) derives the properties & methods of another class (parent / base)


class Car:


class ToyotaCar(Car):


'''

'''

# its a single inheritence

class Car:

    color = "white"
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stooped")


class ToytaCar(Car):
    def __init__(self , name):
        self.name = name


car1 = ToytaCar("Fortuner")
car2 = ToytaCar("prius")

print(car1.name)

print(car1.start())

print(car1.color)

'''
# inheritence

# types
'''
1) single inheritence
2) multi level inheritence
3) multiple inheritence
'''


'''
#2) multi level inheritence
class Car:

  
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stooped")


class ToyotaCar(Car):
    def __init__(self , brand):
        self.brand = brand


class Fortuner(ToyotaCar):
    def __init__(self , type):
        self.type = type


car1 = Fortuner("diesel")
car1.start()

'''
'''
class A:
    varA = "welcome to class A"


class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "wwelcome to class C"


c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

'''

# Super method

'''
super() method is used to access methods of the parent class
'''

'''
class Car:

    def __init__(self, type):
        self.type = type


    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stooped")


class ToytaCar(Car):
    def __init__(self , name, type):
        self.name = name
        super().__init__(type)
        super().start()


car1 = ToytaCar("Fortuner","electric")
print(car1.type)
print(car1.start())

'''




# class methods




'''
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name

    
p1 = Person()
p1.changeName("Ali")
print(p1.name)
print(Person.name)


# it didn't change class name ,instead created a name for object
'''

'''
# now it's changed the name using class directly
class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name

    
p1 = Person()
p1.changeName("Ali")
print(p1.name)
print(Person.name)

'''
'''
class Person:
    name = "anonymous"

    def changeName(self, name):
      self.__class__.name = name

    
p1 = Person()
p1.changeName("Ali")
print(p1.name)
print(Person.name)

'''
# class Methods

'''
A class method is bound to the class & receives the class as an implicit first argument


Note => static method can't access or modify class state & generally for utility

'''

'''
class Person:
    name = "anonymous"

    #def changeName(self, name):
     # self.__class__.name = name
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

     

    
p1 = Person()
p1.changeName("Ali")
print(p1.name)
print(Person.name)

'''

# types

# static methods => doesn't change or interfer with object or class properties

# class methods(cls) => are refer to class proerties 

# instance methods (self) = > deals with objects





# property decorator


'''
class Student:
    def __init__(self, phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"    


stu1 = Student(98 , 97 , 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)
stu1.calcPercentage()
print(stu1.percentage)


'''

# better approch, using property decorator
'''

class Student:
    def __init__(self, phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"    


stu1 = Student(98 , 97 , 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)


'''

# homewrok problem for  decotator , study  getter setter 


#Polymorphism

# polymorphism : operator overloading
'''
when the same operator is allowed to have different meaning according to the context
'''

# practical example
'''
# its also called implicit overloading , python has already done for us
print(1 + 2) # 3
print(type(1))

print(" my " + "college") # concatenation
print(type("my"))

print([1,2,3,4,5] + [6,7,8,9,10]) # merge
print(type([1,2,3]))
'''


# now defining our own

# example complex number's
#1)
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i + ", self.img, "j")

    def add(num1,num2):
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal , newImg)

num1 = Complex(1,7)
num1.showNumber()


num2 = Complex(4,5)
num2.showNumber()


num3 = num1.add(num2)
num3.showNumber()
#print(num3)

'''
'''
# it's not posible right now
num3 = num1 + num2
num3.showNumber()
'''

#  opearors & dunder functions
'''
we define meaning of operator according to our own logic
a + b # addition  a.__add__(b)
'''
#2)
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i + ", self.img, "j")

    def __add__(num1,num2): # making it dunder function
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal , newImg)

num1 = Complex(1,7)
num1.showNumber()


num2 = Complex(4,5)
num2.showNumber()


num3 = num1 + num2
num3.showNumber()
'''

#3)
'''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real , "i + ", self.img, "j")

    def __add__(num1,num2): # making it dunder function
        newReal = num1.real + num2.real
        newImg = num1.img + num2.img
        return Complex(newReal , newImg)
    
    def __sub__(num1,num2): # making it dunder function
        newReal = num1.real - num2.real
        newImg = num1.img - num2.img
        return Complex(newReal , newImg)

num1 = Complex(1,7)
num1.showNumber()


num2 = Complex(4,6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()


num3 = num1 - num2
num3.showNumber()

'''

# let's practice some question's

#q1
'''
define a circle class to create  a circle with radius r using the constructor.
(r)

define an Area() method of the class which calculates the area of the circle.
(pi*r^2)

define a Perimeter() method of the class , which allows you to calculate the perimeter of the circle
(2 * pi * r)

'''
'''
class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())


'''


#q2
'''
define an employee class with attributes role , department & salary, this class also has a showclassdetails() method.

create an engineer class that inherits its properties from employee & has additional attributes: name & age
'''


class Employee:

    def __init__(self, role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    
    def showDetails(self):
        print("role =" , self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)



class Engineer(Employee):

    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75000")


e1 = Employee("accountant","finance","70000")
e1.showDetails()


engg1 = Engineer("Ali khan", 37)
engg1.showDetails()


# let's practice some more question

#q3
''''
create a class order which stores item & its price.

use dunder function __gt__() to convert that:

order1 > order2 if price of order 1 > price of order2
'''

class Order:

    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("chips" , 25)
odr2 = Order("tea", 35)

print(odr1 > odr2)