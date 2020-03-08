import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

# Use the iris database to answer the following questions:

iris = sns.load_dataset('iris')

'''
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
...	...	...	...	...	...
145	6.7	3.0	5.2	2.3	virginica
146	6.3	2.5	5.0	1.9	virginica
147	6.5	3.0	5.2	2.0	virginica
148	6.2	3.4	5.4	2.3	virginica
149	5.9	3.0	5.1	1.8	virginica
150 rows × 5 columns
'''

# What does the distribution of petal lengths look like?

plt.figure(figsize=(16,9))
sns.distplot(iris.petal_length)

'''The distribution of petal lengths appears to be bimodal. There might be a need to further investigate by saperating the flowers into their own groups.'''

# Is there a correlation between petal length and petal width?

plt.figure(figsize=(16,9))
sns.regplot(x='petal_length', y='petal_width', data=iris)

'''The scatter plot shows two distinct groups, and that there is a positive correlation between petal length and petal width.'''

#Would it be reasonable to predict species based on sepal width and sepal length? Which features would be best used to predict species?

sns.pairplot(iris, hue='species')

'''Using a pair plot, with hue seperation applied to the different flower species, we can see that sepal length and sepal width has a clear distinction between setosa and vericolor/virinica. However, the later two are fairly entangled, and would present issue trying to parse them just from those features. If, however, we look at the petal width and petal length features, we can start to see clear patterns emerge based on species.'''

#Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?

#Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

anscombe = sns.load_dataset('anscombe')
anscombe

'''
0	I	10.0	8.04
1	I	8.0	6.95
2	I	13.0	7.58
3	I	9.0	8.81
4	I	11.0	8.33
5	I	14.0	9.96
6	I	6.0	7.24
7	I	4.0	4.26
8	I	12.0	10.84
9	I	7.0	4.82
10	I	5.0	5.68
11	II	10.0	9.14
12	II	8.0	8.14
13	II	13.0	8.74
14	II	9.0	8.77
15	II	11.0	9.26
16	II	14.0	8.10
17	II	6.0	6.13
18	II	4.0	3.10
19	II	12.0	9.13
20	II	7.0	7.26
21	II	5.0	4.74
22	III	10.0	7.46
23	III	8.0	6.77
24	III	13.0	12.74
25	III	9.0	7.11
26	III	11.0	7.81
27	III	14.0	8.84
28	III	6.0	6.08
29	III	4.0	5.39
30	III	12.0	8.15
31	III	7.0	6.42
32	III	5.0	5.73
33	IV	8.0	6.58
34	IV	8.0	5.76
35	IV	8.0	7.71
36	IV	8.0	8.84
37	IV	8.0	8.47
38	IV	8.0	7.04
39	IV	8.0	5.25
40	IV	19.0	12.50
41	IV	8.0	5.56
42	IV	8.0	7.91
43	IV	8.0	6.89
'''

sns.relplot(x='x', y='y', col='dataset', data=anscombe)
plt.show()