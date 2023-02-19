print("hello world"); print("water")

x = 1 + 2
print(x)

y = 1 + 2 \
   + 3
print(y)

name = "John"

if name == "John":
    print(name)

# Note
# Use whitespace and indentation correctly
# Read the output when you encounter an error


# Commenting code
# Explain what the code is intended to do 
# Let developers know that code is deprecated
# Add TODO comments for work to be completed at a later time
# There are different types of comments: Single comments, Multi-line comments and inline comments


# naming conventions

#camelCase -> myName
#snakecase -> my_name

intA = 5
int_a = 6

print(intA)
print(int_a)

#declare multiple variables to assign to single value
a = b = c = 10
print(a)
print(b)
print(c)

# multiple assignments
a,b,c = 1,2,3
print(a)
print(b)
print(c)

#variable assignment
a = 5
print(a)

a= 10
print(a)

# deleting variable
# f = 20
# del f
# print(f)

# Basic data types

# Numeric, Sequence, Dictionary, Boolean, Set, Boolean
# Numeric (Integer, Float, Complex Number)
# Sequence (String, List, Tuples)

# Type function ()


# sequence
# String - sequence of characters enclosed either in single or double quotes

# name = "Jim"
# type(name)
# <class 'str'>

# List - sequence of one or more different or similar types

# example_list = [1, 'hello', 4.5]
#type(example_list)
# <class 'list'>

# Tuple - similar to list but are immutable
# example_tuple = (1, 'hello', 4.5)
# type(example_tuple)
# <class 'tuple'>

# Dictionary - store data in a key value object structure
# ed = {'a': 1, 'b': 2, 'c': 3}
#type(ed)
# <class 'dict'>


# Boolean - true or false
# type(True)
# <class 'bool'>

# set - is an unordered and non-indexed collection of non-repeated values
# example_set = {1, 'hello', 4.5, 'A'}
# type(example_set)
# <class 'set'>

# Your code(python code) -> encoding unicode -> Binary code

# single line 
varA = "Hello world"

# multi line 
varB = "This is too \
big to fit \
on a single line so \
i multi-lined it"

print(varA, varB)

name = "John"
print(name[0])

#len() method
print(len(name))

# String concatenation
str_one = "your"
str_two = " face"
str_three = str_one + str_two
print(str_three)

# formatting strings
# "f-strings"
num_times = 20
print(f'I have told you {num_times} times already!')

# input()
# This function looks for default input device, your keyboard and captures the value.This value can then be assigned or used

print("Where do you live?")
location = input()
print(f"So you live in {location}")

# user input and console output
email = input("Please enter your email address: ")
print(email)

# print arguments
# comma separated -> print(1,2,3)
# arthimetic -> print(1+3)
# string concatentation -> name = 'John' age = 24 -> print(name + age)

# Print function also has reserved keywords can be passed as additional arguments
# object(s) -> values that are printed on screen, sep -> how objects be pretended as separated, end -> defines what get printed at the end 
# file - specifies where values get printed to "stdout"
# flush - boolean expression to flush the buffer - Essentially move data from temporary storage to computer permanent storage

print('Hello', 'you!', sep=', ')

# Direct formatting
a = 10
b = 5
ans = a + b
print("Adding the value of {} and {} = {}" .format(a, b, ans))

# Output formatting
print("I like {0} more than {1}" .format("oranges", "grapes"))

# creating functions

# without paramaters
def say_hello():
    return "Hello there!"

# with parameters
def say_hello(you):
    return "Hello " + you

# type casting
# Explicit and implicit conversion
# popular built in functions: str(), int(), float()
# ord(), hex(), oct(), tuple(), list(), dict(),set()

id = '848274827'
print(int(id))

num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
results = int(num1) + int(num2)

print(f"Your first number is {num1} and second number is {num2} and your results are {results}")

# Operations: mathematical, Logical and conditional

# Mathematical: +, -, /, %, *
# Logical: and, or, not 

# Control flow: refers to the order in which the instructions in a program are executed. 
# Two types of control flow: (if/else, else if -> elif) and Loops(for loop and while loop)

# conditional flow controls: if/else, elif

bill_total = 114
discount1 = 10

if bill_total > 100:
    print("Bill is greater than 100!")
    bill_total -= discount1
else:
    print("Bill is less than 100!")

print("Total bill: " + str(bill_total))

# match statement to use instead of if statement
# match statement compares a value to several different conditions until one is met

http_status = 200

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Not found")
    case 500 | 501:
        print("Server error")
    case _:
        print("Unknown")


# Looping constructs
# Looping is used to iterate through the sequence and access each item inside the sequence
# For loop 
# for (variable) in (sequence):

str = 'Looping' # sequence

for item in str: # iterate
    print (item)

for i in range(0):
    print(i)

favorites = ['Creme Brulee', 'Apple pie', 'Churros', 'Tiramisu', 'Chocolate Pie']

# for item in favorites:
#     print('...', item)

# in a standard for loop dont have access to the index instead can use enumerate func
for idx, item in enumerate(favorites):
    print(idx, item)


# count = 0

# while count < len(favorites):
#     print ('I like ', favorites[count])
#     count += 1

# Nested for loops

# outer loop
for x in range(10):
    print(x)
    #inner loop
    for y in range(10):
        print(y)






