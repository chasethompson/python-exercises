from pydataset import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data('mpg', show_doc=True) # view the documentation for the dataset
# mpg = data('mpg') # load the dataset and store it in a variable


# Copy the code from the lesson to create a dataframe full of student grades.

np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

# randomly generate scores for each student for each subject
# note that all the values need to have the same length here
math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)

# Create a column named passing_english that indicates whether each student has a passing grade in reading.

df['passing_english'] = df.reading > 70

# Sort the english grades by the passing_english column. How are duplicates handled?

df.sort_values(by='passing_english', ascending=False)

# Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first, and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. (Hint: you can pass a list to the .sort_values method)

df.sort_values(by=['passing_english', 'name'])

# Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.

df.sort_values(by=['passing_english', 'english'])

# Calculate each students overall grade and add it as a column on the dataframe. The overall grade is the average of the math, english, and reading grades.

overall_grade = (df.math + df.english + df.reading) / 3
df['overall_grade'] = (df.math + df.english + df.reading) / 3

# Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:

mpg = data('mpg')
mpg.head()

# How many rows and columns are there?

mpg.info()
mpg.shape
"""11 columns"""
"""234 rows"""

# What are the data types of each column?

mpg.dtypes.value_counts()

"""
object     6
int64      4
float64    1
dtype: int64
"""

# Summarize the dataframe with .info and .describe

mpg.info()

"""
<class 'pandas.core.frame.DataFrame'>
Int64Index: 234 entries, 1 to 234
Data columns (total 11 columns):
manufacturer    234 non-null object
model           234 non-null object
displ           234 non-null float64
year            234 non-null int64
cyl             234 non-null int64
trans           234 non-null object
drv             234 non-null object
cty             234 non-null int64
hwy             234 non-null int64
fl              234 non-null object
class           234 non-null object
dtypes: float64(1), int64(4), object(6)
memory usage: 21.9+ KB

"""

mpg.describe()

"""
	displ	year	cyl	cty	hwy
count	234.000000	234.000000	234.000000	234.000000	234.000000
mean	3.471795	2003.500000	5.888889	16.858974	23.440171
std	1.291959	4.509646	1.611534	4.255946	5.954643
min	1.600000	1999.000000	4.000000	9.000000	12.000000
25%	2.400000	1999.000000	4.000000	14.000000	18.000000
50%	3.300000	2003.500000	6.000000	17.000000	24.000000
75%	4.600000	2008.000000	8.000000	19.000000	27.000000
max	7.000000	2008.000000	8.000000	35.000000	44.000000

"""

# Rename the cty column to city.

mpg.rename(columns={'cty': "city"})

# Rename the hwy column to highway.

mpg.rename(columns={'hwy': "highway"})

# Do any cars have better city mileage than highway mileage?

mpg[mpg.cty > mpg.hwy]

# Create a column named mileage_difference this column should contain the difference between highway and city mileage for each car.

mpg['mileage_difference'] = mpg.hwy - mpg.cty

# Which car (or cars) has the highest mileage difference?

mpg['mileage_difference'].max()
mpg[mpg.mileage_difference >= 12]

"""
	manufacturer	model	displ	year	cyl	trans	drv	cty	hwy	fl	class	mileage_difference
107	honda	civic	1.8	2008	4	auto(l5)	f	24	36	c	subcompact	12
223	volkswagen	new beetle	1.9	1999	4	auto(l4)	f	29	41	d	subcompact	12

"""

# Which compact class car has the lowest highway mileage? The best?

mpg = mpg.rename(columns={'class': "car_class"})
compact_cars = mpg[mpg.car_class.str.contains('compact')]
compact_cars.hwy.min()
compact_cars[compact_cars.hwy == 20]
compact_cars.hwy.max()
compact_cars[compact_cars.hwy == 44]

# Create a column named average_mileage that is the mean of the city and highway mileage.

mpg['average_mileage'] = (mpg.cty + mpg.hwy) / 2

# Which dodge car has the best average mileage? The worst?

mpg[mpg.manufacturer.str.contains('dodge')].sort_values(by='average_mileage').head(4) # The worst

mpg[mpg.manufacturer.str.contains('dodge')].sort_values(by='average_mileage', ascending=False).head(1) # The best

# Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:

Mammals = data('mammals')
Mammals.head()

# How many rows and columns are there?

Mammals.shape

"""

(107, 4)

"""

# What are the data types?

Mammals.dtypes.value_counts()

"""
float64    2
bool       2
dtype: int64

"""

# Summarize the dataframe with .info and .describe

Mammals.info()

"""

<class 'pandas.core.frame.DataFrame'>
Int64Index: 107 entries, 1 to 107
Data columns (total 4 columns):
weight      107 non-null float64
speed       107 non-null float64
hoppers     107 non-null bool
specials    107 non-null bool
dtypes: bool(2), float64(2)
memory usage: 2.7 KB

"""

Mammals.describe()

"""

weight	speed
count	107.000000	107.000000
mean	278.688178	46.208411
std	839.608269	26.716778
min	0.016000	1.600000
25%	1.700000	22.500000
50%	34.000000	48.000000
75%	142.500000	65.000000
max	6000.000000	110.000000

"""
# What is the the weight of the fastest animal?

Mammals.speed.max()
Mammals[Mammals.speed >= 110]

Mammals[Mammals.speed >= 110].head(1).weight


# What is the overal percentage of specials?

special = Mammals[Mammals.specials == True] # 10 animals with a special label marked True
""" 9.34579439% """ # 10 / 107

# How many animals are hoppers that are above the median speed? What percentage is this?

hoppers = Mammals[Mammals.hoppers == True]
hoppers[hoppers.speed > 48]
"""6.542056% """ # 7 / 107

