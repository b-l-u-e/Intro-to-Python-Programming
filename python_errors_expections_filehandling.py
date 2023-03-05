# syntax errors - are caused by human errors such as typos or misspelling
# exceptions - which are known errors that need to be handled

# ZERO DIVISION ERROR
def divide_by(a, b):
    return a / b

# try:
#     ans = divide_by(40, 0)
# except Exception as e:
#     print("Something went wrong!", e)
#     print(e.__class__)

try:
    ans = divide_by(40,0)
except ZeroDivisionError as e:
    print(e, "We cannot divide by zero")
except Exception as e:
    print(e, "Something went wrong")

# INDEX ERROR
# Trying to locate an item from list that does not exist

try:
    items = [1,2,3,4,5]
    item = items[6]
    print(item)
except IndexError as e:
    print(e, "Item doesnt exist in the list")


# FILE NOT FOUND ERROR
# Trying to look for a file that doesn't exist

try: 
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e, "File could not found")

# File handling
# Opening, reading and writing files built-in functions 

# open function -  reading, writing and creating files
# open(<FILE_NAME> <FILE_LOCATION>, <MODE>)
# MODE - Indicates what action required either reading, writing or creating 
# output format - specify if u want the file to be text or binary format 


# MODE SETS
# Mode = 'r' -> open and read(text format)
# Mode = 'rb' -> open and read(binary format)
# Mode = 'r+' -> open for reading and writing
# Mode = 'w' -> open for writing 
# open(<FILE_NAME>, a) -> open for editing or appending data

# close function - closing the open file connection and takes no arguments
# close()

# open and close the file connection
# with open('testing.txt', 'r') as file: -> closes the file automatically no close function needed

file = open('test.txt', mode='r')

data = file.readline()

print(data)

file.close()

# OR

with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)

# Files - are used to permanently store data so it is available for future use or as a permanent record

with open('newfile.txt', 'w') as file:
    file.write("This is a new file created!")

with open('newfile.txt', 'w') as file:
    file.writelines(["Another one", "\nTesting if it is working"])

# add to the file 
try:
    with open('newfile.txt', 'a') as file:
        file.writelines(["\nAnother one", "\nTesting if it is working"])
except FileNotFoundError as e:
       print("ERROR", e)

# read() -> Print as a string that contains all the characters
# with open(samplefile.txt, 'r') as file:
#    print(file.read())
#    print(file.read(40)) ->  pass in 40 and print only the first 40 characters

# readline() -> returns a single line as a string