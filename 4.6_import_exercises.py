# 1. Import and test 3 of the functions from your functions exercise file.

import function_exercises 

assert function_exercises.is_two(2) == True
assert function_exercises.is_two('two') == False

from function_exercises import is_two

assert is_two(2) == True
assert is_two('two') == False

from function_exercises import is_two as is_it_two

assert is_it_two(2) == True
assert is_it_two('two') == False

import function_exercises

assert function_exercises.is_vowel('c') == False
assert function_exercises.is_vowel('a') == True

from function_exercises import is_vowel

assert is_vowel('c') == False
assert is_vowel('a') == True

from function_exercises import is_vowel as is_this_a_vowel

assert is_this_a_vowel('c') == False
assert is_this_a_vowel('a') == True

import function_exercises

assert function_exercises.is_consonant('a') == False
assert function_exercises.is_consonant('c') == True

from function_exercises import is_consonant

assert is_consonant('a') == False
assert is_consonant('c') == True

from function_exercises import is_consonant as is_this_a_consonant

assert is_this_a_consonant('a') == False
assert is_this_a_consonant('c') == True

# 2. For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
# How many different ways can you combine two of the letters from "abcd"?

from itertools import product

product_list = list(product('abd', '123'))
product_count = len(product_list)
print(product_count)

from itertools import combinations_with_replacement

combo_list = list(combinations_with_replacement('abcd', 2))
combo_count = len(combo_list)
print(combo_count)

# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:



# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users

import json

json.load(open("profiles.json"))
profile = json.load(open("profiles.json"))

# Total number of users
users = len(profile)

# Number of active users
active_user = [user for user in profile if user['isActive'] == True]




print(len(profile))
 
