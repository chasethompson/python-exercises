# Below CV stands for Class Version upon whole class review

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

product_list = list(product('abd', [1,2,3]))
product_count = len(product_list)
print(product_count)

from itertools import combinations_with_replacement

combo_list = list(combinations_with_replacement('abcd', 2))
combo_count = len(combo_list)
print(combo_count)

from itertools import combinations

combonation_list = list(combinations('abcd', 2))
combonation_count = len(combonation_list)
print(combo_count)

# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:

import json
from pprint import pprint
json.load(open("profiles.json"))
profile = json.load(open("profiles.json"))

profile[0]
profile[0].keys()

[profile['guid'] for profile in profile[:4]]
[profile['balance'] for profile in profile[:4]]

pprint(profile)

# 1. Total number of users
users = len(profile)
print(f"We have a total user base of {users}.")

# 2. Number of active users
[profile['isActive'] for profile in profile]
active_user = [user for user in profile if user['isActive'] == True]
len(active_user)
print(f"We have {len(active_user)} active users out of {users} total users in the system.")

"""
#CV

active_user = [user for user in profile if user['isActive'] # Didn't need == True, as it already would return true.

"""

# 3. Number of inactive users
inactive_user = [user for user in profile if user['isActive'] != True]
len(inactive_user)
print(f"We have {len(inactive_user)} inactive users out of {users} total users in the system.")

"""
#CV

active_user = [user for user in profile if not user['isActive'] # added not instead of != True

"""

# 4. Grand total of balances for all users

total_balance = sum([float(profile["balance"].strip("$").replace(",", "")) for profile in profile])
total_balance
print(f"The total balance for all users is ${total_balance}.")

"""

#CV

[profile['balance'] for profile in profile]

profile = profile[0]
float(profile['balance'].replace('$', '').replace(',',''))

# Basically did what I did, but making it a function allows you to reuse. Start doing this.
def get_profile_balance(profile):
    return float(profile['balance'].replace('$', '').replace(',',''))

[get_profile_blance[profile] for profile in profile]

sum([get_profile_blance[profile] for profile in profile])

"""

# 5. Average balance per user

avg_balance = round((total_balance / users), 2)
avg_balance
print(f"The average balance across all users is ${avg_balance}.")

"""
#CV

balances = [get_profile_blance[profile] for profile in profile]
avg_balance = sum(balance) / len(balance)

# Don't use round on the data, round in the explicit instance you need it rounded.

print(f"That average balance is {avg_balance:,.2f}")

"""

# 6. User with the lowest balance

lowest_bal = min([profile['balance'] for profile in profile])
lowest_bal
user_with_low_bal = ([profile['name'] for profile in profile if profile['balance'] == lowest_bal])
user_with_low_bal
print(f"Our user with the lowest balance is {user_with_low_bal}.")

"""
#CV

user_with_lowest_balance = profile[0]

for use in profiles[1:]:
    get_profile_balance(user) < get_profile_balance(user_with_lowest_balance):
        user_with_lowest_balance = user
user_with_lowest_balance

min(profiles, key=get_profile_balance)['name']

"""

# 7. User with the highest balance

highest_bal = max([profile['balance'] for profile in profile])
highest_bal
user_with_high_bal = [profile['name'] for profile in profile if profile['balance'] == highest_bal]
user_with_high_bal
print(f"Our user with the highest balance is {user_with_high_bal}.")

"""
#CV

max(profiles, key=get_profile_balance)['name']

"""
 
# 8. Most common favorite fruit

max_favorite_fruits = max([profile['favoriteFruit'] for profile in profile])
max_favorite_fruits
print(f"The most popular fruit among our users is {max_favorite_fruits}.")

"""
#CV

"""

# 9. Least most common favorite fruit

min_favorite_fruits = min([profile['favoriteFruit'] for profile in profile])
min_favorite_fruits
print(f"By far {min_favorite_fruits}s are the least popular fruit among our users.")

"""
#CV

"""

# Or you could import Counter
from collections import Counter

fruits = Counter([profile['favoriteFruit'] for profile in profile])
most_common_fav = fruits.most_common(1)[0][0]
least_common_fav = fruits.most_common()[-1][0]

# With Counter() we see apple has the lowest number

# 10. Total number of unread messages for all users

user_greeting = [profile['greeting'] for profile in profile]
user_greeting
user_unread_message = list(map(lambda sub:int(''.join([num for num in sub if num.isnumeric()])), user_greeting))
total_unread = sum(user_unread_message)
total_unread
print(f"Our users have a total of {total_unread} unread messages.")

# Using RegEx to solve for the unread messages

import re
profile_greeting = [re.sub('[^0-9]+', '', profile["greeting"]) for profile in profile]
profile_greeting
def total_unread(l):
    return sum([int(i) for i in l if type(i) == int or i.isdigit()])
total_unread(profile_greeting)

"""

#CV

profile = profile[0]
greeting = profile['greeting']

# Quick and dirty way to find all numbers, not optimal at all.
[profile['greeting'][-19:-17].strip() for profile in profile]

# More robust and easily readable
def get_n_unread_message(profile):
    greeting = profile['greeting']
    start_index = greeting.index('have') + 5
    end_index = greeting.index(' unread')
    return int(greeting[start_index:end_index])

sum([get_n_unread_message(profile) for profile in profile])

# This works also, but only the string only has digits we carry about.
int(''.join[char for char in greeting if char.isdigit()])

"""