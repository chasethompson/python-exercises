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

import json

json.load(open("profiles.json"))
profile = json.load(open("profiles.json"))

# 1. Total number of users
users = len(profile)

# 2. Number of active users
active_user = [user for user in profile if user['isActive'] == True]
len(active_user)

# 3. Number of inactive users
inactive_user = [user for user in profile if user['isActive'] != True]
len(inactive_user)

# 4. Grand total of balances for all users

total_balance = sum([float(profile["balance"].strip("$").replace(",", "")) for profile in profile])
total_balance

# 5. Average balance per user

avg_balance = round((total_balance / users), 2)
avg_balance

# 6. User with the lowest balance

# Lines below were my first attempt
# lowest_bal = min([float(profile["balance"].strip("$").replace(",", "")) for profile in profile]) 
# user_with_low_bal = [user['name'] for user in profile if user['balance'] == lowest_bal]

lowest_bal = min([profile['balance'] for profile in profile])
lowest_bal
user_with_low_bal = [profile['name'] for profile in profile if profile['balance'] == lowest_bal]
user_with_low_bal

# 7. User with the highest balance

highest_bal = max([profile['balance'] for profile in profile])
highest_bal
user_with_high_bal = [profile['name'] for profile in profile if profile['balance'] == highest_bal]
user_with_high_bal
 
# 8. Most common favorite fruit

max_favorite_fruits = max([profile['favoriteFruit'] for profile in profile])
max_favorite_fruits

# 9. Least most common favorite fruit

min_favorite_fruits = min([profile['favoriteFruit'] for profile in profile])
min_favorite_fruits

# Or you could import Counter
from collections import Counter

Counter([profile['favoriteFruit'] for profile in profile])

# With Counter() we see apple has the lowest number

# 10. Total number of unread messages for all users

user_greeting = [profile['greeting'] for profile in profile]
user_greeting
user_unread_message = list(map(lambda sub:int(''.join([ele for ele in sub if ele.isnumeric()])), user_greeting))
total_unread = sum(user_unread_message)
total_unread


