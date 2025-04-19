
#list
# a built-in data type that stores set of values
# it can store elements of different types (integers,float,string etc)

#Lists are the most common structure in Python for array-like data, with more flixibility
# so in python arrays => list

#why we need list
marks1 = 10.1
marks2 = 21.2
marks3 = 17.2

stu1 ="ali"
stu2 = "ahmed"
stu3 = "abbas"

#list
marks = [94.1, 87.21, 91.2,32.2]
print(marks)

print(type(marks))

print(marks[0])
print(marks[1])


student = ["Ali",95.21,"ahmed","abbas",21.03,298.2]
print(student)

#note
# string and python list are very related but
# string => immutable
#list => mutable

#example

str = "hello"
print(str[0]) # access is allowed
#str[0] = "y" # it's not allowed


student = ["Ali",95.21,"ahmed","abbas",21.03,298.2]
print(student[0]) 
student[0] = "_is_ali"
print(student)


# when we access the element in list , make sure that index exist,otherwise error

student = ["Ali",95.21,"ahmed","abbas",21.03,298.2]
#print(student[6]) # it will result in error


#list slicing

marks = [85,94,76,48]
print(marks[1:3])
print(marks[:3])
print(marks[2:])
print(marks[-4:-1])

#list methods

#list.append(2)adds one element at the end

list = [2,1,3]
list.append(10)
print(list)

#list.sort() sorts in ascending order

list = [2,1,3,10,2,0.2]
list.sort()
print(list)


#list.sort(reverse = True) # sort in descending order

list = [2,1,3,10,2,0.2] 
list.sort(reverse = True)
print(list)

# it's also possibile fro strings case
list = ["banana","litchi","apple"]
list.sort(reverse = True)
print(list)


#list.reverse()   # it reverse the string in random order without keep ion mind the sequence

list = ["a","d","e","f"]
list.reverse()
print(list)


#list.insert(idx , el) # insert element at index

list = [2,1,3,10,21]
list.insert(2,11.2)
print(list)


#list.remove(3) # it removes first occurence of element 3

list = [2,1,3,1]
list.remove(1)
print(list)


#list.pop(idx) #removes element at idx

list = [3,4,3,2,5]
list.pop(2)
print(list)



# now topic is 

# Tuple
# a built-in data type that let's create immuatble sequences of values

tup = (87,64,33,95,73)
print(type(tup))

print(tup[0])
print(tup[1])

# tup[0] = 21  # this not allowed

tup = (87,64,33,95,73)
# tuple slicing
print(tup[1:4])

# tuple method

# tuple.index(el) # retrun's index of first occurence

tup = (2,1,3,1)
print(tup.index(3))

#tuple.count(el) # return's the total occurence

tup = (2,1,3,1)
print(tup.count(3))

#now practice some questions

# for list

#q1
# write a program to ask the user to enter names of their 3 favourites movies & store them in a list

movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
 
#q2 
# write a function , to check if a list contains a palindrome of elements .(hint : use copy() method)

# palindrome are those if er read them from start or last ,it's same
# example maam , racecar 

list1 = [1,2,1]
list2 = [1,2,3]


copy_list = list1.copy()
copy_list.reverse()

if (copy_list == list1):
    print("it's a palindrome")
else:
    print("it's not a palindrome")

# for tuple's

#q1
# write a program , to count the number of student's with  "A" grade in the following tuple.

grades  = ("C","D","A","A","B","B","A")

print(grades.count("A"))


#q2
# store the above values in a list & sort them from "A" to "D"

grade  = ("C","D","A","A","B","B","A")
grades = list(grade)  # Convert the tuple to a list#
grades.sort()
print(grades)

