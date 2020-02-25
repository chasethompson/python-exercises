# Working with files exercise file, notes at bottom

# 1. Read the contents of your last exercise file into a variable.

import_exercises = "4.6_import_exercises.py"

with open(import_exercises) as f:
    print(f.read())

# a. Print out every line in the file

with open(import_exercises, "r") as f:
    contents = f.readlines()
    for line in contents:
        print (line)

# b. Print out every line in the file, but add a line numbers

with open(import_exercises, "r") as a, open(import_exercises, "w") as b:
    index = 1
    for line in a:
        b.write("{:4d}: {}\n".format(index, line.rstrip()))
        index += 1

# Better way to handle 1b

with open(import_exercises, "r") as f:
    contents = f.readlines()
    for i, line in enumerate(contents, start = 1):
        print(i + " : " + line)


# 2. Write some python code to create a grocery list.

# a. Create a variable named grocery_list. It should be a list, and the elements in the list should be a least 3 things that you need to buy from the grocery store.

grocery_list = ['milk', 'bread', 'eggs', 'bananas']

# b. Create a function named make_grocery_list. When run, this function should write the contents of the grocery_list variable to a file named my_grocery_list.txt.

def make_grocery_list(grocery_list):
    with open("my_grocery_list.txt", "a") as f:
        f.write(str(grocery_list))

# Class Version

def make_grocery_list(grocery_list):
    filename = "my_grocery_list.txt"
    with open(filename, "a") as f:
        for item in grocery_list:
            f.write(item + "\n")

# c. Create a function named show_grocery_list. When run, it should read the items from the text file and show each item on the grocery list.

def show_grocery_list(grocery_list):
    with open("my_grocery_list.txt") as f:
        print(f.read())

#Class Version

def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        contents = f.readlines()
        for item in contents:
            print(item)

show_grocery_list()

# d. Create a function named buy_item. It should accept the name of an item on the grocery list, and remove that item from the list.

def buy_item(item):
    if item in grocery_list:
        grocery_list.remove(item)
    new_grocery_list = grocery_list
    with open("my_grocery_list.txt", "w") as f:
        f.write(str(new_grocery_list))
    return grocery_list

# Class Version

def buy_item(item, grocery_list):
    grocery_list.remove(item)
    make_grocery_list(grocery_list)
buy_item("spinach", grocery_list)



"""
# Notes

filename = "desktop/something.txt"

with open(filename) as f:
    contents = print(f.read())

contents.split(',')

with open(filename) as f:
    contents = f.readlines()

contents

with open(filename, "a") as f: # Open the file for writing. Will append to any existing contents.
    f.write("Sandwich")

with open(filename) as f:
    print(f.read())

fruits = ["kiwi\n", "apple\n", "banana\n", "pineapple\n"]
with open(filename, "a") as f:
    f.writelines(fruits)

fruits = ["kiwi", "apple", "banana", "pineapple"]
with open(filename, "a") as f:
    for fruit in fruits:
        f.writelines(fruit + "\n")
"""