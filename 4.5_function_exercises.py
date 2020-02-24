# Function Exercises ** Notes at the bottom **

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

def is_two(num):
    if type(num) == str:
        if num.isdigit():
            num = int(num)
    if type(num) == int:
        if num == 2:
            return True
        else:
            return False
    else:
        return False


""" Class Version

def is_two(x):
    return x == 2 or x == '2' """

# To test this function

assert is_two(2) == True
assert is_two('two') == False
assert is_two('2') == True
assert is_two(3) == False

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(word):
    if str(word).isdigit():
        return False
    word = word.lower()
    if word in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
    
""" Class Version

def is_vowel(letter):
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'i'

# or

def is_vowel(letter):
    return len(letter) == 1 and letter.lower() in 'aeiou'

# or

def is_vowel(letter):
    print("----------")  <---- Common debugging technique, putting a print in your function
    vowels = 'aeiou'
    print('[is_vowel] starting')
    # check if the letter in any is vowel
    for vowel in vowels:
        print("[is_vowel] checking vowel: " + vowel)
        if letter.lower() == vowel:
            print("[is_vowel] letter, " + letter + " is a vowel: " + vowel)
            return True
    print("[is_vowel] finished the for loop, our letter is not a vowel")
    # the letter is not in our vowel list
    return False

"""

assert is_vowel('c') == False
assert is_vowel('z') == False
assert is_vowel('a') ==  True
assert is_vowel('i') == True
assert is_vowel('A') == True
assert is_vowel('ae') == False

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(word):
    if str(word).isdigit():
        return False
    word = word.lower()
    if word not in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

""" # Class Version

def is_consonant(letter):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return len(letter) == 1 and letter.isalpha() in letters and not is_vowel(letter) """

assert is_consonant('a') == False
assert is_consonant('b') == True
assert is_consonant('I') == False
assert is_consonant('W') == True

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

vowel = ['a', 'e', 'i', 'o', 'u']
def capitalize_word(word):
    if str(word).isdigit():
        return False
    word = word.lower()
    if word[0] in (vowel):
        return word
    else:
        return word.title()

""" # Class Version

def capitalize_if_consonant(word):
    first_letter == word[0]
    if is_consonant(first_letter):
        return word.capitalize()
    else:
        return word """

assert capitalize_word('codeup') == 'Codeup'
assert capitalize_word('curie') == 'Curie'
assert capitalize_word('aardvark') == 'aardvark'

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip, bill):
    if tip < 0 or tip > 1:
        return False
    else:
        return f"You should tip ${(tip * bill):.10} for a total of ${(tip * bill + bill):.10}."

""" # Class Version

def calculate_tip(tip_percent, bill):
    amount_to_tip = bill * tip_percent
    return amount_to_tip """

assert calculate_tip(.20, 20) == 4.0
assert calculate_tip(.15, 20) == 3.0
assert calculate_tip(.10, 20) == 2.0

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount):
    if discount < 0 or discount > 100:
        return f"You need to put a discount between 1 and 100 percent."
    return f"Sweet, you have a {discount}% discount. So, your total is ${(original_price - discount / 100 * original_price):.2f}"


""" # Class Version

def apply_discount(org, dis):
    discount_amount = org * dis
    return org - discount_amount """

assert apply_discount(10, .10) == 9.0
assert apply_discount(10, .20) == 8.0
assert apply_discount(10, 1) == 0
assert apply_discount(10, 0) == 10


# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(user_input):
    if ',' in user_input:
        user_input = int(user_input.replace(',','_'))
    return user_input

""" # Class Version

def handle_commas(numeric_string):
    string_without_commas = numeric_string.replace(',', '')
    actual_number = int(string_without_commas)
    return actual_number """

assert handle_commas('1,234') == 1234
assert handle_commas('345') == 345
assert handle_commas('9,101,111') == 9101111


# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(grade):
    if grade >= 88:
        return print("Noice, an A")
    elif grade >= 80:
        return print("Solid showing with a B")
    elif grade >= 67:
        return print("C get degrees")
    elif grade >= 60:
        return print("Dun dun dunnnn, you got a D")
    else:
        return print("See you after class, you got an F")

""" #Class Version
 
def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    else:
        return 'F' """


assert get_letter_grade(90) == 'A'
assert get_letter_grade(99) == 'A'
assert get_letter_grade(60) == 'F'
assert get_letter_grade(80) == 'B'

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    output = ''
    for letter in word:
        if letter not in vowel:
            output += letter
            word = output
    return word

""" # Class Version
def remove_vowels(string):
    string_without_vowels = ''
    for c in string:
        if not is_vowel += c
    return string_without_vowels

def remove_vowels(string):
    return ''.join([c for c in string if not is_vowel(c)])' """

assert remove_vowels('a') == ''
assert remove_vowels('Codeup') == 'Cdp'
assert remove_vowels('aaa') == ''
assert remove_vowels('ccc') == 'ccc'

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
#   Name will become name
#   First Name will become first_name
#   % Completed will become completed

def normalize_name(name):
    for letter in name:
        if not letter.isidentifier() and letter != " ":
            name = name.replace(letter, " ")
    name = name.lower()
    name = name.strip()
    name = name.replace(" ","_")
    return name

""" # Class Version

def remove_special_characters(string):
    return ''.join([c for c in string if c.isalnum() or c != ' '])

def normalize_name(string):
    without_special_chars = remove_special_characters(string)
    return without_special_chars.lower().strip().replace(' ', '_') """

assert normalize_name('Name') == name
assert normalize_name('First Name') == first_name
assert normalize_name('% Completed') == completed

# 11. Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumsum(number_string):
    total = 0
    outlist = []
    for num in number_string:
       total += int(num)
       outlist.append(total)
    return outlist

""" # Class Version
def cumsum(numbers):
    total = 0
    cumulative_sum = []
    for n in numbers:
        total += n
        cumulative_sum.append(total)
    return cumulative_sum """

assert cumsum([1, 1, 1]) == [1, 2, 3]
assert cumsum([1, 2, 3, 4]) == [1, 3, 6, 10]

# ** Bonus ** Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

def twelveto24(time):
    """Converts 12 hours time format to 24 hours
    """
    time = time.replace(' ', '')
    time, half_day = time[:-2], time[-2:].lower()
    if time[:2] == "12" and half_day == "am":
        return "00" + time[2:]
    elif half_day == "am":
        return time
    elif time[:2] == "12" and half_day == 'pm':
        return time
    elif half_day == 'pm':
        split = time.find(':')
        if split == -1:
            split = None
        return str(int(time[:split]) + 12) + time[split:]
    else:
        print("You didn't finish with AM or PM.")

assert twelveto24('12:45AM') == '00:45'
assert twelveto24('12:45PM') == '12:45'
assert twelveto24('10:45AM') == '10:45'
assert twelveto24('10:45PM') == '22:45'



# ** Bonus ** Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.

def col_index(col_str):
    """ Convert base26 column string to number. """
    expn = 0
    col_num = 0
    for char in reversed(col_str):
        col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
        expn += 1

    return col_num

assert col_index('A') == 1
assert col_index('Z') == 26
assert col_index('XFD') == 16384


# Notes
# to make your own function, we need to define it first

def increment(x):
    return x + 1

# Functions are first class in Python

# Lambdas are anonymous functions
# Lambdas are one line, only
# think of it as f(x) = x + 1
add_one = lambda x: x + 1 # returns our implicit

add_one(3)

# Mulitple retruns

def sum_and_product(a, b):
    return a + b, a * b

result = sum_and_product(2, 3)

result

a, b = sum_and_product(2, 3)

a

b

# Docstring are a way to add a comment to a function

def increment(x):
    """
    returns a number plus on
    """
    return x + 1

# Keyword Arugments and Default Values
# Arguments go into functions

def greet(greeting = "Hello", recipient = "World"):
    return greeting + ", " + recipient + "!"

greet()
greet("Howdy", "Peeps")
greet(recipient = 'Horses')

# Recursion example

total = 0
total = total + 1 # Iced tea
total = total + 7 # Define the value in terms of itself

def song_that_never_ends():
    print("This is the song that never ends. It goes on and on my friends...")
    print("Other lyrics")
    song_that_never_ends()

def factorial(number):
    if number == 1:         # This is the base case
        return number
    else:
        return number * factorial(number -1)       # Recur towards the

factorial(5)