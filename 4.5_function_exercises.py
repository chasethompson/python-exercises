# Function Exercises * Notes at the bottom *

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

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(word):
    if str(word).isdigit():
        return False
    word = word.lower()
    if word in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False
    
# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(word):
    if str(word).isdigit():
        return False
    word = word.lower()
    if word not in ['a', 'e', 'i', 'o', 'u']:
        return True
    else:
        return False

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

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

def calculate_tip(tip, bill):
    if tip < 0 or tip > 1:
        return False
    else:
        return f"You should tip ${(tip * bill):.10} for a total of ${(tip * bill + bill):.10}."

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount):
    if discount < 0 or discount > 100:
        return f"You need to put a discount between 1 and 100 percent."
    return f"Sweet, you have a {discount}% discount. So, your total is ${(original_price - discount / 100 * original_price):.2f}"

# 7. Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

def handle_commas(user_input):
    if ',' in user_input:
        user_input = int(user_input.replace(',','_'))
    return user_input

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

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(word):
    output = ''
    for letter in word:
        if letter not in vowel:
            output += letter
            word = output
    return word

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


# ** Bonus ** Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

def twelveto24(time):
    time = time.lower()
    if time[-2:] == 'am' and time[:2] == "12":
        return "00" + time[2:-2]
    elif time[-2:] == "am":
        return time[:-2]
    elif time[-2] == "pm" and time[:2] == "12":
        return time[:-2]
    else:
        return str(int(time[:2]) + 12) + time [2:5]

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