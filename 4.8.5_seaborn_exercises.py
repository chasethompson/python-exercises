import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pydataset as data
​
import seaborn as sns

from env import host, user, password

# Use the iris database to answer the following questions:

iris = sns.load_dataset('iris')
iris

# What does the distribution of petal lengths look like?

plt.figure(figsize=(16,9))
sns.distplot(iris.petal_length)

# The distribution of petal lengths appears to be bimodal. There might be a need to further investigate by saperating the flowers into their own groups.
# Is there a correlation between petal length and petal width?

plt.figure(figsize=(16,9))
sns.regplot(x='petal_length', y='petal_width', data=iris)

#The scatter plot shows two distinct groups, and that there is a positive correlation between petal length and petal width.

# Would it be reasonable to predict species based on sepal width and sepal length? Which features would be best used to predict species?

sns.pairplot(iris, hue='species')

# Using a pair plot, with hue seperation applied to the different flower species, we can see that sepal length and sepal width has a clear distinction between setosa and vericolor/virinica. However, the later two are fairly entangled, and would present issue trying to parse them just from those features. If, however, we look at the petal width and petal length features, we can start to see clear patterns emerge based on species.

sns.set(style="darkgrid")

# Subset the iris dataset by species

setosa = iris.query("species == 'setosa'")
virginica = iris.query("species == 'virginica'")
versicolor = iris.query("species == 'versicolor'")

# Set up the figure

f, ax = plt.subplots(figsize=(16, 16))
ax.set_aspect("equal")

# Draw the two density plots

ax = sns.kdeplot(setosa.sepal_width, setosa.sepal_length,
    cmap="Reds", shade=True, shade_lowest=False)

ax = sns.kdeplot(virginica.sepal_width, virginica.sepal_length,
    cmap="Blues", shade=True, shade_lowest=False)

ax = sns.kdeplot(versicolor.sepal_width, virginica.sepal_length,
    cmap="Greens", shade=True, shade_lowest=False)

# Add labels to the plot

red = sns.color_palette("Reds")[-2]
blue = sns.color_palette("Blues")[-2]
green = sns.color_palette("Greens")[-2]

ax.text(2.5, 8.2, "virginica", size=16, color=blue)
ax.text(3.8, 4.5, "setosa", size=16, color=red)
ax.text(2, 5.5, "versicolor", size=16, color=green)

plt.show()

# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?
# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

anscombe = sns.load_dataset('anscombe')
anscombe

sns.lmplot(x='x', y='y', col='dataset', hue="dataset", data=anscombe)
plt.show()

sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=anscombe,
    col_wrap=2, ci=None, palette="muted", height=4,
    scatter_kws={"s": 50, "alpha": 1})

# Load the InsectSprays dataset and read it's documentation.

insect_sprays = pydataset.data("InsectSprays")
pydataset.data("InsectSprays",show_doc=True)
InsectSprays

# Create a boxplot that shows the effectiveness of the different insect sprays.

plt.figure(figsize=(16, 9))
sns.boxplot(data=insect_sprays, y='count', x='spray', hue='spray')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()

# Load the swiss dataset and read it's documentation.

swiss = pydataset.data('swiss')
pydataset.data('swiss', show_doc=True)
swiss

swiss.head()


# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)

swiss['is_catholic'] = swiss.Catholic >= 50
swiss.head()


# Does whether or not a province is Catholic influence fertility?

sns.boxplot(data=swiss, y='Fertility', x='is_catholic')
plt.xlabel("\nPercentage Province is Catholic")
plt.ylabel('Fertility Rate\n')
plt.title("Does Being a Catholic Province Influence Fertility?\n")
xticks, labels = plt.xticks()
labels = ['Less than 50%', 'Greater than 50%']
plt.xticks(xticks, labels)

plt.show()

# What measure correlates most strongly with fertility?

correlation_swiss = swiss.drop(columns=["is_catholic"])

swiss_corr = correlation_swiss.corr()
plt.figure(figsize=(12,12))
sns.heatmap(swiss_corr[['Fertility']].sort_values(by='Fertility', ascending=False),
    vmin=-1,
    cmap='coolwarm',
    annot=True);

b, t = plt.ylim() # discover the values for bottom and top
b += 0.5 # Add 0.5 to the bottom
t -= 0.5 # Subtract 0.5 from the top
plt.ylim(b, t) # update the ylim(bottom, top) values

plt.show()

# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

def get_db_url(username, hostname, password, db_name):
    return f"mysql+pymysql://{user}:{password}@{host}/{db_name}"

query = '''
    SELECT * 
    FROM orders
'''

url = get_db_url(user, host, password,'chipotle')

orders = pd.read_sql(query, url)

orders['price_val'] = orders.item_price.apply(lambda x: float(x.replace('$','').replace(',','')))
item_revenues = orders.groupby('item_name').price_val.agg(['count', 'sum']).sort_values(['count','sum'], ascending = False)
item_revenues['item'] = item_revenues.index
item_revenues = item_revenues.rename(columns={'count':'orders', 'sum':'revenues'})

top_items = item_revenues.sort_values(by='revenues', ascending=False)[:4]
top_items

'''
orders	revenues	item
item_name			
Chicken Bowl	726	7342.73	Chicken Bowl
Chicken Burrito	553	5575.82	Chicken Burrito
Chips and Guacamole	479	2201.04	Chips and Guacamole
Steak Burrito	368	3851.43	Steak Burrito
'''

plt.figure(figsize=(16, 9))
pal = sns.color_palette("Blues_d", len(top_items))

chart = sns.barplot(x='item', y='revenues', data=top_items)

for p in chart.patches:
    chart.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = "center", xytext = (0, 10), textcoords = 'offset points')

plt.show()

# Load the sleepstudy data and read it's documentation.

sleep_study = pydataset.data('sleepstudy')
sleep_study.head()

pydataset.data('sleepstudy', show_doc=True)
sleepstudy

# Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

reaction_by_days_per_subject = sns.lmplot(x='Days', y="Reaction", col='Subject', col_wrap=6, data=sleep_study)
reaction_by_days_per_subject.set(xlim=(0,10), ylim=(190, 500))

plt.show()

plt.figure(figsize=(16, 9))
sns.lineplot(data=sleep_study, y='Reaction', x='Days', hue='Subject')

plt.show()

plt.figure(figsize=(16,9))
sns.lineplot(x='Days', y='Reaction', hue='Subject', data=sleep_study)
sns.lineplot(x='Days', y='Reaction', data=sleep_study, estimator='mean')

plt.show()