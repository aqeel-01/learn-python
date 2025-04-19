

#loops

#loops are used to repeat instructions



#p1

count = 1 #iterator
while count <= 5 :
    print("hello")
    count = count + 1

print(count) 



#p2
i = 1
while i <= 5 :
    print("hello", i)
    i = i + 1



#p3 

i = 1
while i <= 5 :
    print(i)
    i += 1
print("loop ended")


#p4
i = 5
while i >= 1 :
    print(i)
    i -= 1
print("loop ended")


#p5 q1
#q1 print numbers from 1 to 100

i = 1
while i <= 100 :
    print(i)
    i += 1


#p6 q2
#q2 print numbers from 100 to 1

i = 100
while i >= 1 : #stoping condition
    print(i)
    i -= 1



#p7 q3
#q3 print the muliplication table

n = int(input("enter a number : "))

i = 1

while i <= 10:
    print(f"{n} * {i} is  = {n * i }")
    i += 1


#p8 q4
#q 4 print the elements of the following list using a loop:
# [1,4,9,16,25,36,49,64,81,100]


nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0

while idx <= len(nums)-1:
    print(nums[idx])
    idx += 1
    


#p9
heroes = ["ironman","thor","superman","batman"]

idx = 0

while idx <= len(heroes)-1:
    print(heroes[idx])
    idx += 1
    



#p 10
#q 5 search for a number x in this tuple using the loop
# (1,4,9,16,25,36,49,64,81,100)


nums = (1,4,9,16,25,36,49,64,81,100,25)
x = 25
i = 0 #initialization

while i < len(nums):
    if (nums[i] == x ):
        print("FOUND at index",i)
    else:
        print("still finding...")
    i += 1






#break statement

i = 0
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")




nums = (1,4,9,16,25,36,49,64,81,100,25)
x = 25
i = 0 #initialization

while i < len(nums):
    if (nums[i] == x ):
        print("FOUND at index",i)
        break
    else:
        print("still finding...")
    i += 1


#continue
# terminates executaion in the current iteration and continue execution of the loop with
#next iteration


i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue #skip
    print(i)
    i += 1




i = 1
while i <= 10:
    if(i % 2 == 0):
        i += 1
        continue
    print(i)
    i += 1





# for loop : are used for sequential traversal . for traversing list,string,tuples etc


nums = [1,2,3,4,5]

for val in nums:
    print(val)



veggies = ["potato","brinjal","ladayfinger","cucumber"]

for val in veggies:
    print(val)



tup = (1,2,35,6,89,10,21)
for num in tup:
    print(num)


str = "university"

for char in str:
    print(char)


# also we can use else with for loop//which in this case executed after the ending iteration of for loop

str = "UNI"

for char in str:
    print(char)
else:
    print("END")



str = "college"

for char in str:
    if(char == 'e'):
        print("e found")
        break
    print(char)
print("END")



# now practice some questions

#q1 
# (using for loop ) print the elements of the following list using a loop
[1,4,9,16,25,36,49,64,81,100]


nums = [1,4,9,16,25,36,49,64,81,100]

for element in nums:
    print(element)


#q2
# search for a number x in this tuple using the loop
nums = (1,4,9,16,25,36,49,64,81,100,49,101)

x = 49

index = 0
for element in nums:
    if (element == x):
        print("number found at index" , index)
    index += 1




# range()
# range functions returns a sequence of numbers, starting from 0 by default , and increments by 1
# 1 by default and stops before a specific number.

#range(start? , stop , step?) # ? means optional

seq = range(10)

for i in seq:
    print(i)



for i in range(15): #range(stop)
    print(i)


for i in range(2,10): #range (start , stop)
    print(i)


for i in range(2,10,2): # range(start, stop , step) step# mean show much to increase with each
    print(i)


# if we wnat to print even numbers we can also use range()

for i in range(2,101,2):
    print(i)



# now practice questions

# using for & range()

# q1 print numbers from 1 to 100

for i in range(1,101):
    print(i)


#q2 print numbers from 100 to 1

for i in range(100,0,-1):
    print(i)



#q3 print the muliplication table of a number n

n = int(input("enter number :  "))

for i in range(1, 11):
    print(n * i)


# pass statement

# pass is a null statement that does nothing, its  a placeholder for future code


for i in range(5):
    pass
if i > 5:
    pass
print("some useful work ")

n = 5
sum = 0
for i in range(1,n+1):
    sum += i
print("total sum is :", sum)





# practice some questions

#q1 WAP to find sum of first n  natural numbers (using while loop)


n = 7
sum  = 0
i = 1

while i <= n:
    sum += i
    i += 1
print("total sum = ",sum)

#q2 WAP to find the factorial of first n numbers (using for loop)

# factorial of n means
# example n =5 then 1*2*3*4*5 (factorial of 5)
# factorial of n , 1*2*3*....*n (factorial of n)


n = 5
fact = 1 # it should be 1 ,otherwise all answer will be mul by 0
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =  ",fact)


#using for loop
n = 5
fact  = 1
for i in range(1 , n+1):
    fact *= i
print("factorial = ", fact)



