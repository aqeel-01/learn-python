
#NOTE => i have added comments multi - to run multiple chunks of code in same file (it may contain same  names of variables etc)

# file i/o in python

#python can be used to perform operations on a file (read & write data)

#types of all files

# 1) text files : .txt , .docx , .log etc
# 2) binary files : .mp4 , .mov , .png , .jpeg etc


# open, read & close file
# we have to open a file before reading or writing

#example
'''
f = open("file_name" , "mode")

sample.txt
demo.docx

r:read  Mode 
w: write Mode 


data = f.read()
f.close()

'''

'''

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()
'''

'''
character       meaning
'r'             open for reading (default)
'w'             open for writing, truncating the file first
'x'             create a new file and open it for writing
'a'             open for writing , appending to the end of the file if it exists
'b'             binary mode
't'             text mode (default)
'+'             open a disk file for updating (reading and writing)   
'''


# reading a file

# data = f.read()  # reads entire file
# data = f.readline() # reads one line at a time

'''

f = open("demo.txt","r")
data = f.read(5)  # reads only first 5 charcter's
print(data)
f.close()



f = open("demo.txt","r")
line = f.readline()  # reads first line
print(line)
f.close()

f = open("demo.txt","r")
line1 = f.readline()  # reads first line
print(line1)
line2 = f.readline()  # reads second line
print(line2)
f.close()



'''


'''

f = open("demo.txt","r")
data = f.read()
print(data)
line1 = f.readline()   # it print's empty space beacuse 
                       # it reads alredy entire file and now assume cursor is at end
print(line1)
line2 = f.readline()  
print(line2)
f.close()

'''


# writing to a file

'''
f = open("demo.txt" , "w")
f.write("this is a new line") # overwrites the entire file




f = open("demo.txt" , "a") # add => append => add at end
f.write("this is a new line) # adds  to the file

'''
'''

f = open("demo.txt" , "w")
f.write("i want to learn python further")
f.close()


f = open("demo.txt" , "a")
f.write(" as i also want to move on data structures and algorithm")
f.close()

f = open("demo.txt" , "a")
f.write(" \n as things are getting worse")
f.close()


f = open("sample01.txt" , "w") # as it didnt exit , it was created by pyhton itself
f.write("it it exist now")
f.close()


f = open("demo.txt" , "r+") # it overwrites the existing file from starting(pointer at start)
f.write(" xyz ")
print(f.read())
f.close()


f = open("demo.txt" , "a+") #  it appends at last (pointer at end)
f.write(" xyz123 ")
f.close()


'''

#with syntax


'''
with open("demo.txt" , "a") as f:
     data = f.read()
'''

'''
with open("demo.txt" , "r") as f:
    data = f.read()
    print(data)               # note , no close file b/c we didnt need it when  we use it => with


with open("demo.txt", "w") as f:
    f.write("new data ")

'''

# deleting a file

'''
using the os Module 

module (like the code library) is a file written by another programmer that generally has a function 
we can use


import os
os.remove(filename)

'''
'''
import os
os.remove("sample02.txt")
'''

# now practice some questions

#q1
'''
# create a new file "practice.txt" using python. add the following data in it:

hi everyone
we are learning i/o
using python
i like programming in python
'''

'''
f = open("sample03.txt" , "w")
f.write(" hi everyone\n we are learning i/o \n using python\n")
f.write("i like programming in python")
f.close()

# same using with 
with open("sample03.txt","w") as f:
    f.write(" hi everyone\n we are learning i/o \n using python\n")
    f.write("i like programming in python")
'''

#q2
# write a program  that replaces occurence of "python" with "java" in above file
'''
with open("sample03.txt","r") as f:
    data = f.read()
new_data = data.replace("python","java")
print(new_data)

with open("sample03.txt","w") as f:
    f.write(new_data)

'''


#q3
# search if the word "learning" exist in the file or not
'''
#1)
with open("sample03.txt" , "r") as f:
    data = f.read()
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("not found!")

#2)
samples = "learning"

with open("sample03.txt" , "r") as f:
    data = f.read()
    if(data.find(samples) != -1):
        print("Found")
    else:
        print("not found!")
          
#3 with function
def check_for_word():
    samples = "learning"
    with open("sample03.txt" , "r") as f:
         data = f.read()
         if(data.find(samples) != -1):
             print("Found")
         else:
              print("not found!")

check_for_word()

'''
#q4
# write a program to find in which line of the file does the word "learning" occur first.
# print -1 , if word is not found

'''

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("sample03.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1


check_for_line()

'''
#q4
# from  a file containing numbers seprated by comma , print the count of even numbers

#1)
with open("sample04.txt","r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

#2)
count = 0
with open("sample04.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count += 1
print(count)

         
















