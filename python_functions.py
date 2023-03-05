#Functions and Data structures
#Function - set of instructions that take an input and return an output
# A function is declared using def keyword followed by name and task to complete
# -> def <function name>(<params>):
# ->      <task to complete>

bill = 175.00

tax_rate = 15
total_tax = (bill * tax_rate) / 100.00

print('Total', total_tax)

# create reusable function

def calculate_tax(bill, tax_rate):
    return (bill * tax_rate) / 100.00
    
print('Total tax:', calculate_tax(175.00, 15))

# Local scope, Enclosing scope, Global scope and built-in scope(LEGB)
# variables within a built-in and global scope are accessible from anywhere in the code


# global_v
global_v = 10

def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print('Access to global', global_v)
        print('Access to enclosed', enclosed_v)
    fn2()

fn1()

# Local scope refers to a variable declared inside a function
# Enclosing scope refers to a function inside a function (nested function)
# Global scope is when a variable is declared outside of a function
# Built-in scope refers to the reserved keywords that python uses for its built-in functions such as print, def, for, in

# Data structures: Built-in structures and User-defined structures
# Built-in structures: List, Tuple, Dictionary, Set -> considered non-primitive data structures they are classed as objects
# User-defined structures: Stack, Queue, Tree, Graph, LinkedList, Hashmap

# Data structures can be mutable or immutable. Example: List is mutable and Tuple is immutable 

# LIST
# Lists are sequence of one or more different or similar datatypes.
# List is a dynamic array that can hold any datatype

# List is based on an index

items = ["pen", "pencil", "books", "rubber"]
print(len(items)) #checking no of elements

tasks = list(range(1,4))
print(tasks)

friends = ["Mick", "Purge", "Alaska"]
print(friends[0])
print(friends[-1]) # can use negative number to index backwards

# check if a value is in a list
print("Ashley" in friends) 

list1 = [1,2,3,4,5]
print(*list1)

print(list1, sep = " ")

# insert function
list1.insert(len(list1), 6)
print(list1, sep = " ")

# append function
list1.append(7)
print(list1, sep = " ")

# extend function
list1.extend([9,10,12])
print(list1, sep = " ")


# To remove items from list
# pop function
list1.pop(-1)
print(list1, sep = " ")

# del function
del list1[-2]
print(list1, sep = " ")

# for loop
for x in list1:
    print('Value:', x)

# Tuple
# -> They are used as data structures and help to create solid well performing code
# Note: declare tuple without using ()
my_tuple = (1, 'strings', 4.5, True, 'strings', 'strings') # OR
my_tuple_second = (1, 'strings', 5.8, False)
print(my_tuple)
print(my_tuple_second)

# count method -> checks for number of occurences for the item
print(my_tuple.count('strings'))
print(my_tuple.index(4.5))

# Sets
set_a = {1,2,3,4,5,6,7}
set_b = {5,6,7,8,9}
print(set_a)

set_a.remove(2)
print(set_a)

set_a.discard(3)
print(set_a)


# union or | 
print(set_a.union(set_b))
print(set_a | set_b)

# intersection or & 
print(set_a.intersection(set_b))
print(set_a & set_b)

# difference method -> gives you elements that are only in set_a and not in set_b
# difference or -
print(set_a.difference(set_b))
print(set_a - set_b)

# symmetric_difference -> all elements that are present in set_a and not in set_b and vice-versa
# symmetric_difference or ^
print(set_a.symmetric_difference(set_b))
print(set_a ^ set_b)

# Note: set is collection of unordered items hence cant print out content based on index
# Hence set is not a sequence

# Dictionaries
# Dictionaries access values based on keys and not in index position.Hence they are faster and more flexible in operation
# key: value pairs

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice', 4: 'Hot Chocolate'}
print(sample_dict[3])

del sample_dict[2]
print(sample_dict)

# declare dict
my_dict = {1: 'Mocha', 2: 'Cafe Latte', 3: 'Iced Coffee', }

# use values()
for value in my_dict.values():
    print(value)
            
# use keys()
for key in my_dict.keys():
    print(key)

# use items()
for key, value in my_dict.items():
    print(f"key is {key}, value is {value}")

# using in with dictionaries
# Does dict have the key?
print(2 in my_dict)

# Does dict have value?
print("Mocha" in my_dict.values())


# Args and Kwargs
# *args and **kwargs 

# *args
def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(2,4,6,8))

def total_bill(**kwargs):
    sum = 0
    for y in kwargs.values():
        sum += y
    return round(sum, 2)

print(total_bill(coffee=2.99, cake=4.55, juice=2.99))

# NOTE: args could pass in any amount of non-keyword variables
# NOTE: kwargs could pass in any amount of keyword arguments

# List of employees find an employee by their employee_id

employee_list = {
    124: {
        "id": "124",
        "name": "John",
        "department": "Kitchen"
    },
    345: {
        "id": "345",
        "name": "Paul",
        "department": "Boardroom"
    }
}

def get_employee_list_from(id):
    return employee_list[id]

print(get_employee_list_from(124))


