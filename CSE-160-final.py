
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
# get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (15,5) 


# In[2]:

df = pd.read_csv("C:\Users\Vineeth\OneDrive\Documents\CSE 160\crime_dataset.csv", low_memory = False)


# In[3]:

df["Weapon"].value_counts().plot(kind = "bar")
plt.title('Deaths Attributable to Various Weapons')


# In[4]:

hdata = df[df['Victim Age']!=998]
sns.kdeplot(hdata['Victim Age'])


# In[5]:

unsolved = df[df["Crime Solved"] != "Yes"]
unsolved['Year'].value_counts().sort_index(ascending=True).plot(kind='line')
plt.title('Number of Unsolved Homicides: 1980 to 2014')


# In[6]:

d4= df[['Victim Race','Year','Crime Solved']]
d4=d4.groupby(by=['Victim Race', 'Year','Crime Solved']).agg({'Crime Solved':'count'})
d4= d4.groupby(level=[0,1]).apply(lambda x:100 * x/x.sum())
fig = plt.figure()
ax = fig.add_subplot(111)
d4.columns=["Solved_count"]

for name, group in d4.groupby(level=0):
    if name!="Unknown":
        group= group.reset_index().drop("Victim Race",1)
        group=group[group["Crime Solved"]=="Yes"]
        ax.plot(group["Year"], group["Solved_count"], label=name)

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)
plt.title('Crime solving rate by victim race')
plt.show()


# In[ ]:



