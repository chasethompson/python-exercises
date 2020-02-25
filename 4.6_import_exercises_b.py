   1: # Below CV stands for Class Version upon whole class review
   2: 
   3: # 1. Import and test 3 of the functions from your functions exercise file.
   4: 
   5: import function_exercises
   6: 
   7: assert function_exercises.is_two(2) == True
   8: assert function_exercises.is_two('two') == False
   9: 
  10: from function_exercises import is_two
  11: 
  12: assert is_two(2) == True
  13: assert is_two('two') == False
  14: 
  15: from function_exercises import is_two as is_it_two
  16: 
  17: assert is_it_two(2) == True
  18: assert is_it_two('two') == False
  19: 
  20: import function_exercises
  21: 
  22: assert function_exercises.is_vowel('c') == False
  23: assert function_exercises.is_vowel('a') == True
  24: 
  25: from function_exercises import is_vowel
  26: 
  27: assert is_vowel('c') == False
  28: assert is_vowel('a') == True
  29: 
  30: from function_exercises import is_vowel as is_this_a_vowel
  31: 
  32: assert is_this_a_vowel('c') == False
  33: assert is_this_a_vowel('a') == True
  34: 
  35: import function_exercises
  36: 
  37: assert function_exercises.is_consonant('a') == False
  38: assert function_exercises.is_consonant('c') == True
  39: 
  40: from function_exercises import is_consonant
  41: 
  42: assert is_consonant('a') == False
  43: assert is_consonant('c') == True
  44: 
  45: from function_exercises import is_consonant as is_this_a_consonant
  46: 
  47: assert is_this_a_consonant('a') == False
  48: assert is_this_a_consonant('c') == True
  49: 
  50: # 2. For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
  51: 
  52: # How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
  53: # How many different ways can you combine two of the letters from "abcd"?
  54: 
  55: from itertools import product
  56: 
  57: product_list = list(product('abd', [1,2,3]))
  58: product_count = len(product_list)
  59: print(product_count)
  60: 
  61: from itertools import combinations_with_replacement
  62: 
  63: combo_list = list(combinations_with_replacement('abcd', 2))
  64: combo_count = len(combo_list)
  65: print(combo_count)
  66: 
  67: from itertools import combinations
  68: 
  69: combonation_list = list(combinations('abcd', 2))
  70: combonation_count = len(combonation_list)
  71: print(combo_count)
  72: 
  73: # Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
  74: 
  75: import json
  76: from pprint import pprint
  77: json.load(open("profiles.json"))
  78: profile = json.load(open("profiles.json"))
  79: 
  80: profile[0]
  81: profile[0].keys()
  82: 
  83: [profile['guid'] for profile in profile[:4]]
  84: [profile['balance'] for profile in profile[:4]]
  85: 
  86: pprint(profile)
  87: 
  88: # 1. Total number of users
  89: users = len(profile)
  90: print(f"We have a total user base of {users}.")
  91: 
  92: # 2. Number of active users
  93: [profile['isActive'] for profile in profile]
  94: active_user = [user for user in profile if user['isActive'] == True]
  95: len(active_user)
  96: print(f"We have {len(active_user)} active users out of {users} total users in the system.")
  97: 
  98: """
  99: #CV
 100: 
 101: active_user = [user for user in profile if user['isActive'] # Didn't need == True, as it already would return true.
 102: 
 103: """
 104: 
 105: # 3. Number of inactive users
 106: inactive_user = [user for user in profile if user['isActive'] != True]
 107: len(inactive_user)
 108: print(f"We have {len(inactive_user)} inactive users out of {users} total users in the system.")
 109: 
 110: """
 111: #CV
 112: 
 113: active_user = [user for user in profile if not user['isActive'] # added not instead of != True
 114: 
 115: """
 116: 
 117: # 4. Grand total of balances for all users
 118: 
 119: total_balance = sum([float(profile["balance"].strip("$").replace(",", "")) for profile in profile])
 120: total_balance
 121: print(f"The total balance for all users is ${total_balance}.")
 122: 
 123: """
 124: 
 125: #CV
 126: 
 127: [profile['balance'] for profile in profile]
 128: 
 129: profile = profile[0]
 130: float(profile['balance'].replace('$', '').replace(',',''))
 131: 
 132: # Basically did what I did, but making it a function allows you to reuse. Start doing this.
 133: def get_profile_balance(profile):
 134:     return float(profile['balance'].replace('$', '').replace(',',''))
 135: 
 136: [get_profile_blance[profile] for profile in profile]
 137: 
 138: sum([get_profile_blance[profile] for profile in profile])
 139: 
 140: """
 141: 
 142: # 5. Average balance per user
 143: 
 144: avg_balance = round((total_balance / users), 2)
 145: avg_balance
 146: print(f"The average balance across all users is ${avg_balance}.")
 147: 
 148: """
 149: #CV
 150: 
 151: balances = [get_profile_blance[profile] for profile in profile]
 152: avg_balance = sum(balance) / len(balance)
 153: 
 154: # Don't use round on the data, round in the explicit instance you need it rounded.
 155: 
 156: print(f"That average balance is {avg_balance:,.2f}")
 157: 
 158: """
 159: 
 160: # 6. User with the lowest balance
 161: 
 162: lowest_bal = min([profile['balance'] for profile in profile])
 163: lowest_bal
 164: user_with_low_bal = ([profile['name'] for profile in profile if profile['balance'] == lowest_bal])
 165: user_with_low_bal
 166: print(f"Our user with the lowest balance is {user_with_low_bal}.")
 167: 
 168: """
 169: #CV
 170: 
 171: user_with_lowest_balance = profile[0]
 172: 
 173: for use in profiles[1:]:
 174:     get_profile_balance(user) < get_profile_balance(user_with_lowest_balance):
 175:         user_with_lowest_balance = user
 176: user_with_lowest_balance
 177: 
 178: min(profiles, key=get_profile_balance)['name']
 179: 
 180: """
 181: 
 182: # 7. User with the highest balance
 183: 
 184: highest_bal = max([profile['balance'] for profile in profile])
 185: highest_bal
 186: user_with_high_bal = [profile['name'] for profile in profile if profile['balance'] == highest_bal]
 187: user_with_high_bal
 188: print(f"Our user with the highest balance is {user_with_high_bal}.")
 189: 
 190: """
 191: #CV
 192: 
 193: max(profiles, key=get_profile_balance)['name']
 194: 
 195: """
 196: 
 197: # 8. Most common favorite fruit
 198: 
 199: max_favorite_fruits = max([profile['favoriteFruit'] for profile in profile])
 200: max_favorite_fruits
 201: print(f"The most popular fruit among our users is {max_favorite_fruits}.")
 202: 
 203: """
 204: #CV
 205: 
 206: """
 207: 
 208: # 9. Least most common favorite fruit
 209: 
 210: min_favorite_fruits = min([profile['favoriteFruit'] for profile in profile])
 211: min_favorite_fruits
 212: print(f"By far {min_favorite_fruits}s are the least popular fruit among our users.")
 213: 
 214: """
 215: #CV
 216: 
 217: """
 218: 
 219: # Or you could import Counter
 220: from collections import Counter
 221: 
 222: fruits = Counter([profile['favoriteFruit'] for profile in profile])
 223: most_common_fav = fruits.most_common(1)[0][0]
 224: least_common_fav = fruits.most_common()[-1][0]
 225: 
 226: # With Counter() we see apple has the lowest number
 227: 
 228: # 10. Total number of unread messages for all users
 229: 
 230: user_greeting = [profile['greeting'] for profile in profile]
 231: user_greeting
 232: user_unread_message = list(map(lambda sub:int(''.join([num for num in sub if num.isnumeric()])), user_greeting))
 233: total_unread = sum(user_unread_message)
 234: total_unread
 235: print(f"Our users have a total of {total_unread} unread messages.")
 236: 
 237: # Using RegEx to solve for the unread messages
 238: 
 239: import re
 240: profile_greeting = [re.sub('[^0-9]+', '', profile["greeting"]) for profile in profile]
 241: profile_greeting
 242: def total_unread(l):
 243:     return sum([int(i) for i in l if type(i) == int or i.isdigit()])
 244: total_unread(profile_greeting)
 245: 
 246: """
 247: 
 248: #CV
 249: 
 250: profile = profile[0]
 251: greeting = profile['greeting']
 252: 
 253: # Quick and dirty way to find all numbers, not optimal at all.
 254: [profile['greeting'][-19:-17].strip() for profile in profile]
 255: 
 256: # More robust and easily readable
 257: def get_n_unread_message(profile):
 258:     greeting = profile['greeting']
 259:     start_index = greeting.index('have') + 5
 260:     end_index = greeting.index(' unread')
 261:     return int(greeting[start_index:end_index])
 262: 
 263: sum([get_n_unread_message(profile) for profile in profile])
 264: 
 265: # This works also, but only the string only has digits we carry about.
 266: int(''.join[char for char in greeting if char.isdigit()])
 267: 
 268: """
