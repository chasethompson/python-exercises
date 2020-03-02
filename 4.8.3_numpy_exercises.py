# Numpy exercises
# Use the following code for the questions below:
# a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there?

neg = a < 0
neg_total = neg.sum()
print(neg_total)

# 2. How many positive numbers are there?

pos = a > 0
pos_total = pos.sum()
print(pos_total)

# 3. How many even positive numbers are there?

pos_even = (a > 0) & (a % 2 == 0)
pos_even_total = pos_even.sum()
print(pos_even_total)

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

plus_3 = a + 3
plus_3_even = (plus_3 > 0) & (plus_3 % 2 == 0)
plus_3_even_total = plus_3_even.sum()
print(plus_3_even_total)

# 5. If you squared each number, what would the new mean and standard deviation be?

np.mean(a)
np.std(a)
print(a.mean())
print(a.std())

squared_a = np.square(a)
print(squared_a)
print(squared_a.mean())
print(squared_a.std())
print(f"The original mean is {a.mean()} and the original standard deviation is {a.std()}. If you square each number, they change to {squared_a.mean()} and {squared_a.std()}, respectively")

# 6. A common statistical operation on a dataset is centering.
# This means to adjust the data such that the center of the data is at 0.
# This is done by subtracting the mean from each data point. Center the data set.

centering_a = a - a.mean()
print(centering_a)

# 7 Calculate the z-score for each data point.

mean = np.mean(a)
std = np.std(a)
z_score_a = (a - mean) / std
print(z_score_a)

# 8

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:

# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = sum(a)
print(sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = min(a)
print(min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = max(a)
print(max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = sum(a) / len(a)
print(mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

def product_of_a(lst):
    result = 1
    for num in lst:
        result = result * num
    return result

print(product_of_a(a))

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

def squares_of_a(lst):
    return [num ** 2 for num in lst]
    
print(squares_of_a(a))

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

def odds_in_a(lst):
    return [num for num in lst if num % 2 == 1]

print(odds_in_a(a))

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

def evens_in_a(lst):
    return [num for num in lst if num % 2 == 0]

print(evens_in_a(a))

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...

## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
# print(sum_of_b)

b = np.array(b)
sum_of_b = np.sum(b)
print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

# min_of_b = min(b)
print(np.min(b))

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.max(b)
print(max_of_b)

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.mean(b)
print(mean_of_b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number

product_of_b = np.product(b)
print(product_of_b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)

squares_of_b = np.square(b)
print(squares_of_b)

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)

odds_in_b = b % 2 == 1
print(b[odds_in_b])

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)

evens_in_b = b % 2 == 0
print(b[evens_in_b])

# Exercise 9 - print out the shape of the array b.

print(b.shape)

# Exercise 10 - transpose the array b.

print(np.transpose(b))

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b = np.reshape(b, (1, 6))
print(b)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b = np.reshape(b, (6, 1))
print(b)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

c = np.array(c)
min_c = np.min(c)
print(min_c)
max_c = (np.max(c))
print(max_c)
sum_c = np.sum(c)
print(sum_c)
product_c = np.product(c)
print(product_c)

# Exercise 2 - Determine the standard deviation of c.

std_c = np.std(c)
print(std_c)

# Exercise 3 - Determine the variance of c.

var_c = np.var(c)
print(var_c)

# Exercise 4 - Print out the shape of the array c

shape_c = np.shape(c)
print(shape_c)

# Exercise 5 - Transpose c and print out transposed result.

transpose_c = np.transpose(c)
print(transpose_c)

# Exercise 6 - Get the dot product of the array c with c. 

print(c.dot(c))

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# dot_c_sum = sum(c * np.dot(c, c))
print((c * c.T).sum())

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

print((c * c.T).prod())

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

d = np.array(d)

sin_d = np.sin(d)
print(sin_d)

# Exercise 2 - Find the cosine of all the numbers in d

cos_d = np.cos(d)
print(cos_d)

# Exercise 3 - Find the tangent of all the numbers in d

tan_d = np.tan(d)
print(tan_d)

# Exercise 4 - Find all the negative numbers in d

neg_d = d < 0
print(d[neg_d])

# Exercise 5 - Find all the positive numbers in d

pos_d = d > 0
print(d[pos_d])

# Exercise 6 - Return an array of only the unique numbers in d.

unique_d = np.unique(d)
print(unique_d)

# Exercise 7 - Determine how many unique numbers there are in d.

size_unique_d = unique_d.size
print(size_unique_d)

# Exercise 8 - Print out the shape of d.

shape_d = np.shape(d)
print(shape_d)

# Exercise 9 - Transpose and then print out the shape of d.

transpose_d = np.transpose(d)
print(np.shape(transpose_d))

# Exercise 10 - Reshape d into an array of 9 x 2

d = np.reshape(d, (9, 2))
print(d)
