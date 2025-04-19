

# NOTE = > i have added multi-line comments for different chunks of code 

# oop in python
'''
 to map with real world scenearios,we started using objects in code
 this is called object oriented programming

 '''

'''
our previous knowledge was
concept of procedural programming
then functions introduced => which helps reuseability and reduce's redundancy in code
now concept of oop => classes => objects => further reuseability of code
'''

# class & object in python

'''
class is a blueprint for creating objects

# creating class

class Student:
      name = "Ali"


#creating object (instances)

s1 = Student()
print(s1.name)


'''
'''
class Student:
    name = "Ali"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)



class Car:
    color = "blue"
    brand = "mercedes"

car1 = Car()
print(car1.color)
print(car1.brand)

'''

#constructor
'''

__init__function

constructor

all classes have a function called __init__() , which is always executed when the object is being initiated



# creating class

class Student:
     def __init__(self, fullname):
         self.name = fullname


# creating object

s1 = Student("Ali)
print(s1.name)


the self parameter is a reference to the current instance of the class , and is used to access variables
that belongs to the class


'''


'''
class Student:
    name = "Ali"
    def __init__(self):
        print("adding new student in database ...")

s1 = Student()

'''

'''
class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("adding new student in database ...")

s1 = Student("ahmed")
print(s1.name)

s2 = Student("Ali")
print(s2.name) # attributes

'''

# attributes
'''
 attributes => data =>variables
'''
'''
# we can also use same name for parameter of function and for self.instance(object)
class Student:
    def __init__(self, fullname,marks):
        self.name = fullname
        self.marks = marks  # same
        print("adding new student in database ...")

s1 = Student("ahmed",23)
print(s1.name,s1.marks) 

s2 = Student("Ali",45)
print(s2.name,s2.marks)

'''

'''
# generally in most cases we use same names like these
class Student:
    def __init__(self, name,marks):
        self.name = name    # same
        self.marks = marks  # same
        print("adding new student in database ...")

s1 = Student("ahmed",23)
print(s1.name,s1.marks) 

s2 = Student("Ali",45)
print(s2.name,s2.marks)

'''
# two types  constructors

# default constructor
# parameterized constructor
'''
class Student:

    # default constructor , if we won't create this python will automatically will create
    def __init__(self):
        pass

    # parameterized constructor
    def __init__(self, name,marks):
        self.name = name    # same
        self.marks = marks  # same
        print("adding new student in database ...")

s1 = Student("ahmed",23)
print(s1.name,s1.marks) 

s2 = Student("Ali",45)
print(s2.name,s2.marks)


'''

#classes & instances Attributes

'''
class.attr => is same for all objects
obj.attr   => is different of all objects
'''

'''
class Student:
     
    college_name = "beyond_college"  # class attribute => it will remain same for all objects, such as college
    def __init__(self, name,marks):
        self.name = name    # object attribute => different => each has his unique name 
        self.marks = marks  # object attribute => different => each has his unique marks
        print("adding new student in database ...")

s1 = Student("ahmed",23)
print(s1.name,s1.marks,s1.college_name) 

s2 = Student("Ali",45)
print(s2.name,s2.marks,s2.college_name)

# we can also access college name for all students as
print(Student.college_name)

'''
'''
# q which will execute if we have same for obj attr and for class attr
class Student:
     
    college_name = "beyond_college"  
    name = "anonymous" # class attr
    def __init__(self, name,marks):
        self.name = name     #  => object attr > class attr (answer)
        self.marks = marks  
        print("adding new student in database ...")

s1 = Student("ahmed",23)
print(s1.name,s1.marks,s1.college_name) 

s2 = Student("Ali",45)
print(s2.name,s2.marks,s2.college_name)

# we can also access college name for all students as
print(Student.college_name)

'''

# Methods

'''
methods are basically functions that belongs to objects


# creating class
class Student:
    def __init__(self,fullname):
        self.name = fullname
    
    def hello(self):
        print("hello",self.name)

# creating object
s1 = Student("Ali)
s1.hello()
'''

'''
class Student:
    college_name = "A college"

    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def welcome(self,greet):
        print("welcome student", self.name)
        self.greet1 = greet
        print(greet)

    def get_marks(self):
        return self.marks


s1 = Student("Ali",21)
s1.welcome("hy")
print(s1.get_marks())

'''
# note in classes =>functions => we call them methods

# let's practice some question's

#q1 
# create Student class that takes name & marks of 3 subjects as arguments in constructor.
# then create a method to print the average

'''
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg marks are",sum/3)


s1 = Student("Ali",[21,28,30])
s1.get_avg()

# also you can change the artibute

s1.name = "Ahmed"
s1.get_avg()

'''
# static methods
'''
methods that don't use the self parameter ( they work at class level)

self.name => they were for object level , but now we want to create for class level
'''
#example
'''
class Student:
    @staticmethod  #decorator
    def college():
        print("collge name is A College")


decorators allow us to wrap another function in order to extend the behaviour of the wrapped
function, without permanently modifying it

=> a decorator is a function takes the function and returns the function,
 just changing the behaviour of that function
'''
'''
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")
    

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg marks are",sum/3)


s1 = Student("Ali",[21,28,30])
s1.get_avg()

# also you can change the artibute

s1.name = "Ahmed"
s1.get_avg()
s1.hello()

'''
# important

# Topic's in oop

#Abstraction
'''
hiding the implementation details of a class and only showing the essential features to the user
'''

'''
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.clutch = True
        print("car started...")

car1 = Car()  
car1.start() # it's just showing the finaal result or essential output , not internal working of class
             # so , this is called abstraction
            

'''

#   Encapsulation
'''
wrapping data and functions into single unit (object) => class
'''



'''
class car:  => its encapsutlation
    # data

    #function1

    # function2

    # function n

'''


# now further practice question's

#q
'''
create account class with 2 attributes- balance & account no.
create methods for debt,credit & printing the balance
'''


class Account:
    
    def __init__(self, bal ,acc):
        self.balance = bal
        self.account_no = acc
    
    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("Rs" , amount ,"was debited")
        print("total balance = ",self.get_balance())

    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs" , amount ,"is credited")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(10000, 123450)
acc1.debit(1000)
acc1.credit(300)

acc1.credit(70000)

