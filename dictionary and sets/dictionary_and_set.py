
# dictionary
# dictionary are used to store data values in key:value pairs
# they are un-ordered, mutable(changeable) & don't allow duplicate keys

info = {
    "key": "value",
    "name": "college",
    "learning": "coding",
    "age": 21 ,
    "is_adult" : True ,
    "marks": 94.21 ,
    "subjects": ["python","c++","rust"], #list in a dictionary
    "topics": ("tuple","dict","list") ,   # tuple in a dictionary
    3.14 : "pi",
    3.12 : 21
    
}

print(type(info))
print(info)

#access values via key

print(info["name"])
print(info["age"])

# updating existing values

info["name"] = "Ali"
print(info)

# adding new values
info["is_exist"] = True
print(info)

# entire creating new dictionary
null_dictionary = {}
print(null_dictionary)
null_dictionary["has_value"] = 2.21
print(null_dictionary)
print(info)


#nested dictionaries

student = {
    "name": "ali",
    "subjects": { # dictionary
        "phy": 97,
        "chem": 92,
        "math" : 91
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["math"])


# dictionary methods

#myDictionary.keys() # returns all keys

student = {
    "name": "ali",
    "subjects": { # dictionary
        "phy": 97,
        "chem": 92,
        "math" : 91
    }
}

print(student.keys())

# we can also convert into list from dictionary using typecasting
print(list(student.keys()))

print(len(student))


#myDictionary.values() # return's all values

print(student.values())

# myDictionary.items() # return's all (key,val) pairs as  tuples

print(student.items())

# access indiviusal ite or pairs
pairs = list(student.items()) # must convert into list for indiviusal access ,otherwise error
print(pairs[0])



#myDictionary.get("key") # return's the key occording to value

student = {
    "name": "ali",
    "subjects": { # dictionary
        "phy": 97,
        "chem": 92,
        "math" : 91
    }
}

# print(student["name3"]) # error
print(student.get("name3")) # no error ->Simply print none => gracefully handled the situation 
#  avoid program crash



#myDictionary.update(newDictionary or key-value pair) # insert the specific items to the dictionary


student = {
    "name": "ali",
    "subjects": { # dictionary
        "phy": 97,
        "chem": 92,
        "math" : 91
    }
}

student.update({"city" : " lahore"})
print(student)


student.update({"city" : " multan","language":"python"})
print(student)


# now topic is 
# set

# set is a collection of the un-ordered items
# each element in the set must be unique & immutable
# we can add bool , int, float,string,tuple, but not list , dictionary

collection  = {1,2,3,4,5,6,7,8}

print(collection)
print(type(collection))


collection  = {1,2,3,"hy","hy",3,2} # it will ignore the duplicates
print(collection) # also it can print values randomly

print(len(collection))


newCollection = set() # empty set , syntax
print(type(newCollection))


# set methods

# v.imp note 
# sets => mutable
# set => element itself => immutable

# set.add(element) # adds an element

newCollection = set()
newCollection.add(2)
newCollection.add(1)
newCollection.add("hy")
newCollection.add(2) # it will be ignored

print(newCollection)


# set.remove(element) # removes the element
newCollection.remove(2)
print(newCollection)

newCollection.add("college")
newCollection.add((1,2,3,4)) # it's tuple
# newCollection.add([1,2,3]) # throw error unhashable
print(newCollection)


#set.clear() # empties the entire set

print(len(newCollection))
newCollection.clear()
print(len(newCollection))

#set.pop() # removes a random value

collection = {"hy","college","coding",2.4,6,7}
print(collection)
print(collection.pop())

print(collection) 


# set union(set2) # combines both set values & return's new

set1 = {1,2,3,4}
set2 = {2,4,5,6,7}
print(set1.union(set2)) 

print(set1)
print(set2)

#set.intersection(set2) # combines common values & return new

set1 = {1,2,3,4}
set2 = {2,4,5,6,7}
print(set1.intersection(set2)) 


#let's practice some questions

#q1
# store following word meanings in a python dictionary:
# table: "a piece of furniture" , "list of facts & figures"
# cat : "a small animal"

word_mean = {
    "table": [ "a piece of furniture" , "list of facts & figures" ], # we can store two values in a tuple or list
    "cat" : "a small animal"
}

print(word_mean)


#q2
# you are given a list of subjects for students . assume one classroom is required for 1  subject
# how many classrooms are needed by all students

# "python","java","c++","python","javascript",
# "java","python","java","c++","c"

subjects = {
    "python","java","c++","python","javascript",
    "java","python","java","c++","c"
}


print(subjects)
print(len(subjects))

#q3
# write a program to enter marks of 3 subjects from the user and store them in dictionary. start with
# an empty dictionary & add one by one . use subjects name as keys & marks as value

marks = {}

x = int(input("enter phy marks:  "))
marks.update({"phy": x})

x = input("enter chem marks:  ")
marks.update({"chem": x})

x = input("enter math marks:  ")
marks.update({"math": x})

print(marks)


#q4
# figure out a way to store 9 & 9.0 as separate values in the set
#(you can take the help of  built-in data types)

values = {
    ("float", 7.0),
    ("int", 7)
}
print(values)


