
#   NOTE i have septared difernt chunks of code with multi-line comments

'''
print("Hello world")

'''


'''
# variables

age = 20

age = 30
print(age)

price = 19.23
print(price)

first_name = "Ali"
print(first_name)

is_online = True
print(is_online)

#excercise

name = input("what is your name ?  ")
print("Hello " + name)

'''

'''
#type conversion

birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(age)
'''


'''
# simple task

first = input("enter your first number")
second = input("enter your second number")

sum = int(first) + int(second)

print("so , the sum of two numbers is" + str(sum))

'''

# strings
'''
course = 'python for begineers'

print(course.upper())

print(course.find('t'))

print(course.replace('for' , '4'))

print('python for ' in course)

'''

'''

#arthemetic operations


print(10 + 13)
print( 10 // 3) # for int result of division
print( 10 / 3) #for float result of division
print(10 ** 4) # exponent



#agumented assingemnt operator
x = 10
x = x + 3
x += 3 

print(x)

'''
'''
#operator precedence

x = 20 + 3 * 2  # result will be 26

# but can be changed using ()

y = (10 + 5 ) * 2  #result will be 30
print(y)

'''
#comparison operator
'''
x = 3 >= 3
print(x)
'''


# operator list
'''
>
>=
<
<=
==
!=

'''




#logical operator
'''
price = 25
print(price > 10 and price < 30)


'''

# logical operator list
'''
and(both)
or (at least one)
not (inverse the result)
'''


# if statement
'''
temperature = 11

if temperature > 30:
    print("its a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("it's a nice day")
elif temperature > 10:
    print("it's a bit cold")
else:
    print("it's cold")
print("if statement was checked")

'''

#excerice

'''
weight = int(input("weight: "))
unit = input("(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs: " + str(converted))

'''


#while loop

'''


i = 1
while i <= 10:
    print(i)
    i = i + 1
'''

'''
i = 1

while i <= 10:
    print(i * '*')
    i = i + 1

'''



#lists
'''
names = ["john ", "bob","mosh", "sam","mary"]
print(names)
print(names[0])
print(names[-1]) # it represent last element
print(names[-2]) # it represent second last element

# modifying the element
names[0] = "jon"
print(names)

# accesing elments of choices
print(names[0:3]) # it will print values at zero index to 2 excluding ending index


'''


#list methods


'''
numbers = [1,2,3,4,5]
numbers.append(6) #appended
print(numbers)


numbers.insert(0, 21)  #inserted at choice of index
print(numbers)

numbers.remove(3)
print(numbers)


# numbers.clear()
print(numbers)

print( 1 in numbers) #check weather the number exist

print(len(numbers))

'''



# for loops
'''
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)


#using same by while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

'''


# the range() function


'''
numbers = range(5)
print(numbers)


numbers = range(5,10)
for number in numbers:
    print(number)


numbers = range(5,10, 2)
for number in numbers:
    print(number)


for number in range(5):
    print(number)


'''



# tuples  
#these are like list but they are immutable

numbers = (1,2,3,2,2,2)
numbers.count(2)