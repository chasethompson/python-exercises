# Conditional Basics

# prompt the user for a day of the week, print out whether the day is Monday or not

is_it_monday = input("What day of the week is it?")

if is_it_monday == "Monday":
    print("Yay! It's Monday!")
else:
    print("Today is not Monday.")

# prompt the user for a day of the week, print out whether the day is a weekday or a weekend

is_it_a_weekday = input("What day of the week is it?")

if is_it_a_weekday == 'Saturday':
    print("Whoop! It's the weekend baby.")
elif is_it_a_weekday == 'Sunday':
    print("Whoop! It's the weekend baby.")
else:
    print("It is not the weekend.")

# create variables and make up values for
    # the number of hours worked in one week
    # the hourly rate
    # how much the week's paycheck will be
    
hours_worked = 40
hourly_rate = 52
weekly_pay = hours_worked * hourly_rate

# write the python code that calculates the weekly paycheck.
# You get paid time and a half if you work more than 40 hours

if hours_worked > 40:
    print(f"You worked overtime at {hours_worked} hours and earned ${int((hourly_rate*1.5)*hours_worked)} this week.")
else:
    print(f"Your worked {hours_worked} hours and earned ${hourly_rate*hours_worked} this week.")

# Loop Basics

# While
# Create an integer variable i with a value of 5.

i = 5

# # Create a while loop that runs so long as i is less than or equal to 15

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

while i <= 1000000:
    print(i)
    i **= 2

# Write a loop that uses print to create the output shown below.

i = 100

while i >= 5:
    print(i)
    i -= 5

# For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.

selected_number = int(input("Please choose a single digit number"))

for i in range(1, 11):
    print(f"{selected_number} x {i} = {selected_number * i}")

# Create a for loop that uses print to create the output shown below.

i = 0

for i in range(10):
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

# Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Display a table of powers.
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

while True:
    number = int(input("Enter a number: "))
    print("Here is your table!")
    for i in range(1, (number + 1)):
        square = i ** 2
        cube = i ** 3
        print(i, square, cube)
    continue_string = input("Would you like to play again? Enter Y or N: ")
    if continue_string.lower() == "y":
        print("Let's do this again.")
        continue
    else:
        print("Have a good day.")
        break

# Convert given number grades into letter grades.

user_grade = input("Enter numerical grade from 0 to 100: ")
for grade in user_grade:
    if grade >= 88:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 67:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")



