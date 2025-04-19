

# strings
# string is a data type that stores a sequence of charcters

str1 = "this is a string"
str2 = " it's a college"
str3 = """this is a string"""

#escape sequence character to seprate sing line into muliple

str1 = "this is a string . \n we are creating in python language"
print(str1)


str1 = "this is a string . \t we are creating in python language" # tab space
print(str1)


# concatination
# joins multiple strings with +

str1 = "my name "
str2 = " is "
str3 = " Ali"
print(str1 + str2 + str3)

final_string = str1 + str2 + str3
print(final_string)


# length of string

str1 = "college"
length = len(str1)
print(length)


str1 = "hy"
str2 = " i'm  "
str3 = " Ali"
print(str1 + " " + str2 + str3)

final_string = str1 +" " + str2 + str3
print(final_string)
print(len(final_string))


#indexing
# indexing in a string help us to access charcters indiviusally

str = "college"
ch = str[0]
print(ch)


#slicing

str = "ourCollege"
print(str[2:6])

print(str[3:len(str)])
print(str[3:])

print(str[: 4]) # it means [0:4]

#slicing (negative index)

str = "apple"
print(str[-5:-1])



#string functions


#string.endswith("er") # returns true if string ends with er

str = "programmer"
print(str.endswith("mer"))



# string.capitalize() # capitalizes the first character

str = "im a programmer"
print(str.capitalize())
print(str)  # it means , it doesnt affect or change the original string


# string.replace(old,new)
str = "im a programmer"
print(str.replace("m","w"))

print(str.replace("im a","pyhton"))


#string.find(word) # returns 1st index of 1st occurrer

str = "college "
print(str.find("g"))
print(str.find("A"))  # if we it didnt exist , -1 index will be return


#string.count("i") # counts the occurrence of that charcter or substring

str = "im a programmer"
print(str.count("m"))


# now practice some questions

#q1
# write a program , to input user's first name and print its length

name = input("enter your first name:  ")
length = len(name)
print("length of your name is " , length)


#q2
# write a program , to find occurence of $ in a string

str = "Hi , $im the $ symbol "
print(str.count("$"))


# conditional Statements

age = 21
if(age >= 18):
    print("can Vote & apply for license")
    print("can drive")

if(True):
    print("can drive")


light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait and look")
print("its end ,all statements are checked")

#how conditions are checked

num = 10

if (num > 5):
    print("greater than 5")
if (num  > 7):
    print(" num is greater than 7") # in this case both if were executed or 
                                    # checked no matter if first one is true


if (num > 5):
    print("greater than 5")
elif (num  > 7):
    print(" num is greater than 7") # in this case if was true , so elif not checked


# use of else

light = "green"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("wait and look")
else:
    print("light is broken")
print("its end ")


age = 23
if(age >= 18):
    print("can vote")
else:
    print("CANNOT VOTE")

# marks and grade with help of conditional statement 

marks = int(input("enter student marks:  "))

if(marks >= 90):
    grade = "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("grade of the student is : ",grade)


#nesting

age = 37

if(age >= 18):
    if(age >= 80):
        print("over aged cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
  


#now practice questions

#q1
# write a program  , if  a number entered by the user is odd or even

num = int(input("enter a number  :  "))

if (num % 2 == 0):
    print("number ",num ,"is even")
else:
    print("number ",num ,"is odd")


#q2
# write a program , to find the greater of 3 numbers entered by the user

num1 = int(input("enter a  first number  :  "))
num2 = int(input("enter a  second number  :  "))
num3 = int(input("enter a third  number  :  "))

if (num1 >= num2 and num1 >= num3):
    print("first number is graeter ",num1)
elif(num2 >= num3):
    print("second number is largest ",num2)
else:
    print("third number is greater ", num3)

# similarly logic for four numbers 

num1 = int(input("enter a  first number  :  "))
num2 = int(input("enter a  second number  :  "))
num3 = int(input("enter a third  number  :  "))
num4 = int(input("enter a fourth  number  :  "))


if (num1 >= num2 and num1 >= num3 and num1 >= num4):
    print("first number is graeter ",num1)
elif(num2 >= num3 and num2 >= num4):
    print("second number is largest ",num2)
elif(num3 >= num4 ):
    print("third number is largest ",num3)
else:
    print("fourth number is greater ", num4)



#q3
# write a program to check , if  a  number is a multiple of 7 or not

num = int(input("enter a number :  "))

if (num % 7 == 0):
    print("entered number ",num , "is muliple of 7")
else:
    print("entered number ",num,"is not multiple of 7")
