# Trying to come up with name for your dog but unsure what to cal your dog
# Start accessing the file which has shortlist of names to choose for your dog
# The file name is petnames.txt
# To import the petnames.txt use "open("petnames.txt", "r")"
# To randomly pick a name import random module

import random

# Use random.choice() function
# choice() accepts a sequence parameter. A list is one of its accepted values


f = open("petnames.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))

# If you had multiple files in your folder, can allow yourself to pick a file from which to read in a list of names

f_name = input('Type the file name: ')
f = open(f_name)  # 'r' omitted as it is the default
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))
