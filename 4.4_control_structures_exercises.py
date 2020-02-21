# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

is_it_monday = input("What day of the week is it?")

if is_it_monday == "Monday":
    print("Yay! It's Monday!")
else:
    print("Today is not Monday.")

# More advanced version

day = input("What day of the week is it? ")

day = day.lower() # lowercase the user input

# Continue prompting the user for the day of the week if their input ain't a day.
while day not in ["monday", "muesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("Please type in the full day of the week.")
    day = input("What day of the week is it today?")
    day = day.lower()

if day.lower() == "monday":
    print("Today is Monday!")
else:
    print(f"Today ain't Monday. It is {day.capitalize()}")

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

is_it_a_weekday = input("What day of the week is it?")

if is_it_a_weekday == 'Saturday':
    print("Whoop! It's the weekend baby.")
elif is_it_a_weekday == 'Sunday':
    print("Whoop! It's the weekend baby.")
else:
    print("It is not the weekend.")

# More advanced answer

day = input("What is the day of the week? ")
day = day.lower()

while day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("Please type in the full day of the week.")
    day = input("What day of the week is it today? ")
    day = day.lower()

if day in ["saturday", "sunday"]:
    print(f"{day.capitalize()} is part of the weekend!")
else:
    print(f"{day.capitalize()} is a weekday day!")

# We could use an OR operator

if day == "saturday" or day == "sunday":
    print(f"{day.capitalize()} is part of the weekend!")
else:
    print(f"{day.capitalize()} is a weekday day!")

# create variables and make up values for
    # the number of hours worked in one week
    # the hourly rate
    # how much the week's paycheck will be
    
hours_worked = 40
hourly_rate = 52
total = 0
weekly_pay = hours_worked * hourly_rate

if hours_worked < 40:
    total = hourly_rate * hours_worked
else:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * 1.5 * hourly_rate
    regular_pay = 40 * hourly_rate
    total = regular_pay + overtime_pay

print(f"Total pay is {total}, after working {hours_worked} for hour rate of {hourly_rate} with overtime - if overtime worked.")

# write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours

if hours_worked > 40:
    print(f"You worked overtime at {hours_worked} hours and earned ${int((hourly_rate*1.5)*hours_worked)} this week.")
else:
    print(f"Your worked {hours_worked} hours and earned ${hourly_rate*hours_worked} this week.")

# Loop Basics

# While
# Create an integer variable i with a value of 5.

i = 5 # Start
end = 15 # Ending number
while i <= end:
    print(i)
    i += 1

# # Create a while loop that runs so long as i is less than or equal to 15

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0

while i <= 100:
    print(i)
    i += 2


# Alter your loop to count backwards by 5's from 100 to -10.

i = 100

while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2

while i < 1_000_000:
    print(i)
    i *= i

# Write a loop that uses print to create the output shown below.

i = 100

while i >= 5:
    print(i)
    i -= 5

# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

number = int(input("Please choose a single digit number "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Create a for loop that uses print to create the output shown below.

for i in range(1, 10):
    print(str(i) * i)

#Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this).

number = input("Please select an odd number between 1 and 50: ")

while int(number) not in range(1,51) or number.isdigit() == False or int(number) % 2 == 0:
    number = input("Please try again, select an odd number between 1 and 50: ")
    continue

# Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

for i in range(1,51):
    if i == int(number):
        continue
    print(i)

# Different version

user_choice = input("Input an odd integer between 1 and 50? ")
while (user_choice.isdigit() == False  # keep prompting user if input is not a whole number
            or int(user_choice) < 1    # keep prompting if they input less than 1.
            or int(user_choice) > 50   # keep prompting if they input higher than 50 
            or int(user_choice) % 2 == 0): # keep prompting if they provided an even number.
    print(f"{user_choice} is nice, but we'll need an odd number between 1 and 50.")
    user_choice = input("Please input an odd number between 1 and 50. ")

user_choice = int(user_choice)

print(f"{user_choice} is an odd number between 1 and 50. Thank you.")

print("The number to skip is", {user_choice})

for i in range(1,50):
    if i % 2 == 0:
        continue

    if i == user_choice:
        print(f"Skipping {i}")
        continue
    print(f"{i} is an odd number.")
    
# The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

user_choice = input("Input a positive number ")
while (user_choice.isdigit() == False
            or int(user_choice) <= 0):
    print(f"{user_choice} is nice, but we'll need a positive number.")
    user_choice = input("Please input a positive number. ")

user_choice = int(user_choice)

for i in range(user_choice + 1):
    print(i)

while user_choice >= 1:
    print(user_choice)
    user_choice -= 1


# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0: # If i is evenly divisible by 3 and 5 print FizzBuzz
        print("FizzBuzz")
    elif i % 3 == 0: # If i is evenly divisible by 3 print Fizz
        print("Fizz")
    elif i % 5 == 0: # If i is evenly divisible by 5 print Buzz
        print("Buzz")
    else:
        print(i)

# Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

# Other Version

user_choice = input("Input a positive number ")
while (user_choice.isdigit() == False
            or int(user_choice) <= 1):
    print(f"{user_choice} is nice, but we'll need a positive number.")
    user_choice = input("Please input a positive number. ")

user_choice = int(user_choice)

print("number | squared | cubed")
for i in range(1, user_choice + 1):
    print(f"{i}      |     {i**2}    | {i**3}")

# First version
while True:
    number = int(input("Enter a number: "))
    print("Here is your table!\n")
    print("|number|squared|cubed|")
    print("|------|-------|-----|")
    for i in range(1, (number + 1)):
        square = i ** 2
        cube = i ** 3
        print("|" + str(i) + "|",square, cube)
    continue_string = input("Would you like to play again? Enter Y or N: ")
    if continue_string.lower() == "y":
        print("Let's do this again.")
        continue
    else:
        print("Have a good day.")
        break
    
# Convert given number grades into letter grades.

# My version

while True:
    grade = float(input("What was your grade, from 0 to 100?\n"))
    if grade >= 88:
        print("Noice, an A")
    elif grade >= 80:
        print("Solid showing with a B")
    elif grade >= 67:
        print("C get degrees")
    elif grade >= 60:
        print("Dun dun dunnnn, you got a D")
    else:
        print("See you after class, you got an F")
    continue_string = input("Would you like to put in another grade? Enter Y or N: ")
    if continue_string.lower() == "y":
        print("Let's see hoe you did.")
        continue
    else:
        print("Have a good day.")
        break


# Clase Version

while True:
    print("Welcome to the grading application!")
    user_choice = input("Please input a positive number. ")
    while (user_choice.isdigit() == False or int(user_choice) < 0 or int(user_choice) >= 100):
        print(f"{user_choice} is nice, but we'll need a positive number.")
        user_choice = input("Please input a positive number. ")

    user_choice = int(user_choice)  
    if user_choice >= 88:
        print("Noice, an A")
    elif user_choice >= 80:
        print("Solid showing with a B")
    elif user_choice >= 67:
        print("C get degrees")
    elif user_choice >= 60:
        print("Dun dun dunnnn, you got a D")
    else:
        print("See you after class, you got an F")
    
    user_choice = input("Do you want to continue? Type Y or Yes. ")
    wants_to_stop = user_choice.lower() not in ["y", "yes"]
    if wants_to_stop:
        break

#Create a list of dictionaries where each dictionary represents a book that you have read.

# My Version

books_i_have_read = [
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "genre": "scifi"
    },
    {
        "title": "Never Split The Difference",
        "author": "Christopher Voss",
        "genre": "self help"
    },
    {
        "title": "Harry Potter and The Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "genre": "fantasy"
    },
    {
        "title": "The Obstacle Is The Way",
        "author": "Ryan Holiday",
        "genre": "philosophy"
    },
    {
        "title": "Stillness Is Key",
        "author": "Ryan Holiday",
        "genre": "philosophy"
    }
]

genre_list = []
for i in books_i_have_read:
    genre_list.append(i["genre"])
while "left brain" != "right brain":
    genre_question = input("What genre would you like to see a book for? ".lower())
    if genre_question in genre_list:
        break
    else:
        print("Sorry, we don't have a book in that genre. Try again ")
for i in books_i_have_read:
    if genre_question == i["genre"]:
        print(i["title"])

# Class Version

books = [
    {
        "title": "Ender's Game",
        "author": "Orson Scott Card",
        "genre": "scifi"
    },
    {
        "title": "Never Split The Difference",
        "author": "Christopher Voss",
        "genre": "self help"
    },
    {
        "title": "Harry Potter and The Prisoner of Azkaban",
        "author": "J.K. Rowling",
        "genre": "fantasy"
    },
    {
        "title": "The Obstacle Is The Way",
        "author": "Ryan Holiday",
        "genre": "philosophy"
    },
    {
        "title": "Stillness Is Key",
        "author": "Ryan Holiday",
        "genre": "philosophy"
    }
]

#for book in books:
#    print(f"{book['title']} by {book['author']} is about {book['genre']}")

genre = input("Please input a genre ")
for book in books:
    if book["genre"] == genre:
        print(book["title"])