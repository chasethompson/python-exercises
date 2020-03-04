## 1. Use pandas to create a Series from the following data:

#["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# a. Name the variable that holds the series fruits.

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# b. Run .describe() on the series to see what describe returns for a series of strings.

fruits.describe()

# c. Run the code necessary to produce only the unique fruit names.

fruits.unique()

# d. Determine how many times each value occurs in the series.

fruits.value_counts()

# e. Determine the most frequently occurring fruit name from the series.

fruits.value_counts().sort_values().tail(1)
"""fruits.value_counts().index[0] # accesses the index at index 0"""

# f. Determine the least frequently occurring fruit name from the series.

fruits.value_counts().sort_values().head(1)
"""fruits.value_counts().index[-1]"""

# g. Write the code to get the longest string from the fruits series.

index_of_longest_string = fruits.apply(len).argmax()

fruits[index_of_longest_string]
# this returns maximum string length

fruits.str.len().max()
# this returns the fruit with the maximum string length

max(fruits, key = len)

# h . Find the fruit(s) with 5 or more letters in the name.

five_or_more_letters = fruits.str.len() > 5
fruits[five_or_more_letters]

# i. Capitalize all the fruit strings in the series.

fruits.str.upper()
"""fruits.str.title()"""

# j. Count the letter "a" in all the fruits (use string vectorization)

fruits.str.count("a")
fruits.str.count('a').sum()

# k. Output the number of vowels in each and every fruit.

def count_vowels(n):
    num_vowels = 0
    for char in n:
        if char in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

fruits.apply(count_vowels)

"""
fruits = fruits.str.lower()

(fruits.str.count("a") 
     + fruits.str.count("e") 
     + fruits.str.count("i") 
     + fruits.str.count("o") 
     + fruits.str.count("u"))
"""

# l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

fruits[fruits.apply(lambda n: n.count('o') > 1)]

# m. Write the code to get only the fruits containing "berry" in the name

fruits[fruits.str.contains('berry')]

# n. Write the code to get only the fruits containing "apple" in the name

fruits[fruits.str.contains('apple')]

# o. Which fruit has the highest amount of vowels?

fruits[fruits.apply(count_vowels).max()]

"""
fruits[(fruits.str.count("a") 
     + fruits.str.count("e") 
     + fruits.str.count("i") 
     + fruits.str.count("o") 
     + fruits.str.count("u")).argmax()]
"""

# 2 Use pandas to create a Series from the following data:


# ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']

amount = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])

# a. What is the data type of the series?

"""

type is object, which means strings

"""

# b. Use series operations to convert the series to a numeric data type.

amount_as_float = amount.replace(r'[\$,]', '', regex=True).astype(float)

"""

or

"""

amount_as_float = amount.str.replace(r'[\$,]', '').astype(float)

# c. What is the maximum value? The minimum?

amount_as_float.max() # max
amount_as_float.min() # min

# d. Bin the data into 4 equally sized intervals and show how many values fall into each bin.

amount_as_float.value_counts(bins=4).sort_index()

"""
(-4511.111, 1197705.993]      7
(1197705.993, 2395133.385]    4
(2395133.385, 3592560.778]    3
(3592560.778, 4789988.17]     6
dtype: int64
"""

"""
bins = pd.cut(prices, 4)
bins.value_counts()
"""

# e. Plot a histogram of the data. Be sure to include a title and axis labels.

plt.figure(figsize=(16, 6))
amount_as_float.plot.hist()
plt.title("Invoice Totals")
plt.xlabel("Invoice Total")

"""
plt.title("price distributions in 4 equal bins")
plt.xlabel("$")
plt.ylabel("# occurences")
plt.hist(prices, bins=4)
plt.show()
"""

# 3. Use pandas to create a Series from the following exam scores:

# [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

# a. What is the minimum exam score? The max, mean, median?

exam_scores.agg(['min', 'max', 'mean', 'median'])
exam_scores.describe()

# b. Plot a histogram of the scores.

plt.figure(figsize=(16,9))
exam_scores.plot.hist()

plt.title("Exam Scores")
plt.xlabel("Grades")
plt.ylabel("Grade Frequency")

# c. Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

def bin_number(n):
    if n < 70:
        return "F"
    elif n < 75:
        return "D"
    elif n < 80:
        return "C"
    elif n < 90:
        return "B"
    else:
        return "A"

letter_grade = exam_scores.apply(bin_number).value_counts().sort_index()

plt.figure(figsize=(16,9))
letter_grade.plot.bar()
plt.title("Letter Grades")
plt.xticks(rotation=0)


# d. Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

max_grade = exam_scores.max()
curve_amount = 100 - max_grade
curve_grades = exam_scores + curve_amount

# 4. Use pandas to create a Series from the following string:

# ['hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy']

gibberish = list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')

gibberish = pd.Series(gibberish)

"""
letters = pd.Series(list(gibberish))
"""

# a. What is the most frequently occuring letter? Least frequently occuring?
 
# Most frequent

gibberish.value_counts().head(1)
"""
letters.value_counts().index[0]
"""

# Least frequent

gibberish.value_counts().tail(1)
"""
letters.value_counts().index[-1]
"""

# 6. How many vowels are in the list?

gibberish.apply(count_vowels).sum()

# c. How many consonants are in the list?

gibberish.str.len().sum() - gibberish.apply(count_vowels).sum()

gibberish[~gibberish.apply(lambda n: n in 'aeiou')].count()

# d. Create a series that has all of the same letters, but uppercased

gibberish.str.upper()

# e. Create a bar plot of the frequencies of the 6 most frequently occuring letters.

six_most_frequent = gibberish.value_counts().head(6)

"""
six_most_frequent = gibberish.value_counts()[:6]

"""

plt.figure(figsize=(16, 9))
six_most_frequent.plot.bar()
plt.title("Six Most Frequently Occuring")
plt.xlabel("Letters")
plt.xticks(rotation=0)
plt.ylabel("Letter Frequency")