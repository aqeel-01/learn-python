

#p1

def cal_sum(a,b):
    sum = a + b
    print(sum)
    return sum

cal_sum(5,20)



cal_sum(2,11)


cal_sum(12,18)


#p2


def cal_sum(a,b): # function defination , parameter
    return a + b

sum = cal_sum(1,2) # function call , argument 
print(sum)


def print_hello():
    print("hello")

print_hello()


out = print_hello()
print(out)


# average of 3 number

def avg_3(a,b,c):
    avg = (a+b+c)/3
    print(avg)

avg_3(12,25,33)



#types of functions

# builtin functions
# user defined functions


#default parameter
# assigning a default value to parameter,which is used when no argument is passed

def cal_prod(a,b= 4):
    print(a * b)
    return a * b
cal_prod(2)


# now practice some questions


#q1 print the length of a list (list is the parameter)

cities = ["lahore","isl","rawlp","mul"]

heroes = ["thor","ironman","captian america"]

def calculate_length(list):
    print(len(list))

calculate_length(cities)
calculate_length(heroes)



#q2
 # write a function to print the elements of a list in a single line (list is the parameter)

heroes = ["thor","ironman","captian america"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()


#q3 write a function to find the factorial of n (n is the parameter)

#same logic in loop
n  = 5
fact = 1
for i in range(1 , n+1):
    fact *= i
print(fact)

# same in functions
def factorial(n):
    fact = 1
    for i in range(1 , n + 1):
        fact *= i
    print(fact)

factorial(5)

# q 4 
# write a function to convert usd to pkr

#till now  1 usd = 280.40 pkr

def converter(usd_val):
    pkr_val = usd_val * 280.40
    print(usd_val, "USD = ", pkr_val , "pkr")

converter(100)


n = int(input("enter a number :  ").strip())

def check_num(n):
    if n % 2 == 0:
        print(n ,"is even ")
    else:
        print(n , "is odd")

check_num(n)


# Recursion

# when a function calls itself repeatedly

def show(n):
    if(n == 0): # base case
        return
    print(n)
    show(n-1)

show(10)


# calculate fcatorial using recursive approch

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(5))


# now practice some questions

#q1
# write a rescursive function to calculate the sum of first n natural numbers


def cal_sum(n):
    if(n == 0):
       return 0
    return cal_sum(n-1) + n

sum = cal_sum(5)

print(sum)


#q 2 write a recursive function to print all elements in a list 
#hint : use list & index as parameter

def print_list(list , idx=0):
    if (idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx + 1)

fruit = ["mango","litchi","apple","banana"]
print_list(fruit)