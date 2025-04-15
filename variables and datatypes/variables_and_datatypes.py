


print("Hello world!")



# variables 
# a variables is a name given to a memory location 


name = "Ali" # string
age = 23    #int
price = 3.42 # float


age2 = age

print("my name is ", name)
print("my age is ", age)


print(type(name))
print(type(age))
print(type(price))



# data types

# integers  +ive ,-ve , 0 
# string    "ali", 'ali'
# float     2.32
# boolean   True , False
# None      a = None







name1 = "hy"
name2 = 'hy'
name3 = '''hy'''

print(name1)
print(name2)
print(name3)



age = 23
old = False
a = None

print(type(old))
print(type(a))


# print sum

a = 2
b =5
sum  = a + b
print( sum)


# comments in python

# singel line comment
"""
muli 
line
comment
"""


# types of operators


#types of opertor

# an operator is a symbol that performs a certain operation between operands

#arithmetic operator
#(+ , - ,* , / , % , **)

#relational / comparison operators 
#( == , != , > , < , >= , <=)

#assingment operator
#(= , += , -= , *= , /= %= , **= )

#logical operator
#( not , and , or)


# arithmetic operator
a = 5
b = 10
sum  = a + b
print(sum)

print(a - b)
print(a + b)
print(a * b)
print( a / b)

print( a % b) #reminder
print( a ** b) # a^b


# relational operator

a = 50
b = 10

print( a==b)

print( a != b) # True

print( a >= b)
print( a > b)
print ( a < b)


# assingment operator

num = 10
num = num + 12 # same as num += 12
print("num is : " ,num)


num = 10
num *= 10
print("num is :  ", num)

num = 10
num /= 10
print("num is : ",num)

num = 10
num %= 2

print("num is : ",num)

num = 10
num **= 5
print("num is : ",num )



# logical operator

print( not True)
print( not False)


a = 50 
b = 30

print( not (a > b))

value_1 = True
value_2 = True

print(" both operator result ", value_1 and value_2)
print(" both operator result ", value_1 or value_2)

value_1 = True
value_2 = False

print(" both operator result ", value_1 and value_2)
print(" both operator result ", value_1 or value_2)

a = 30
b = 20
print("OR operator",(a==b) or (a > b))


# Type conversion

# type conversion (python automatically)
# type casting    (user manually)

# type conversion
a = 2
b = 3.45
sum = a + b

print(sum)

# type casting

a = int("2")  # a = int("Ali") it should not work , when we typecast we should
              # know that it should be compatibel somehow
b = 4.32
sum = a + b
print(type(a))
print("sum is", sum)


num = 3.12
num =  str(num)

print(type(num))



# how to take user input

name = input("enter your name :  ")
print("welcome  ", name)

value = input("enter some value  :  ")
print(type(value), value)   # so the point is , input function return the string

#so we can type cast
value = int(input("enter  a value :  "))
print("so value is ",value)
print(type(value))

name = input("enter your name : ")
age = int(input("enter your age :  "))
marks = float(input ("enter your marks:  "))

print("welcome ", name)
print("age = ", age)
print("marks = ",marks)


# now practice some questions

#q1
# write a program to input 2 numbers & print their sum

num1 = float(input("enter a first number :  "))
num2 = float(input("enter a second number :  "))

sum = num1 + num2
print(" sum of two numbers is : ",sum)


#q2
# write a program to input side of a square & print its area

side = float(input("enter square side :  "))
area = side * side
print("area is ", area)


#q3
# write a program to input 2 floating point numbers & print thier average

a = float(input("enter first number : "))
b = float(input("enter second number  : "))


avg = (a+b)/2
print("avg is = ",avg)

#q4
# write a program to input 2 int numbers , a and b
#print True if  a is greater than or equal to b . if not print False


a = int(input("enter first number : "))
b = int(input("enter second number  : "))

c = a >= b

print("result is  = ",c)