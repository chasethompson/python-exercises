# Functions

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