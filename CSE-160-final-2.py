
import pandas as pd
import numpy as np
# get_ipython().magic(u'matplotlib inline')
# import matplotlib.pyplot as plt
# import seaborn as sns
# plt.rcParams["figure.figsize"] = (18,7)
import csv 
from operator import itemgetter


def visual():

    df = pd.read_csv("crime_dataset.csv", low_memory = False)


    # In[80]:

    df["Weapon"].value_counts().plot(kind = "bar", color = "LightGreen")
    plt.title('Deaths Attributable to Various Weapons')


    # In[83]:

    hdata = df[df['Victim Age']!=998]
    hdata["Victim Age"].value_counts().plot(kind = "bar", color = "purple")


    # In[78]:




# In[90]:

    unsolved['Year'].value_counts().sort_index(ascending=True).plot(kind='line', color = "Red")
    plt.title('Number of Unsolved Homicides: 1980 to 2014')


    # In[4]:

    dict_states = {'Alaska':'AK','Alabama':'AL','Arkansas':'AR','Arizona':'AZ', 'California':'CA', 'Colorado':'CO', 'Connecticut':'CT',
    'District of Columbia':'DC', 'Delaware':'DE', 'Florida':'FL', 'Georgia':'GA', 'Hawaii':'HI', 'Iowa':'IA',
    'Idaho':'ID', 'Illinois':'IL', 'Indiana':'IN', 'Kansas':'KS', 'Kentucky':'KY', 'Louisiana':'LA',
    'Massachusetts':'MA', 'Maryland':'MD', 'Maine':'ME', 'Michigan':'MI', 'Minnesota':'MN', 'Missouri':'MO',
    'Mississippi':'MS', 'Montana':'MT', 'North Carolina':'NC', 'North Dakota':'ND', 'Nebraska':'NE',
    'New Hampshire':'NH', 'New Jersey':'NJ', 'New Mexico':'NM', 'Nevada':'NV', 'New York':'NY', 'Ohio':'OH',
    'Oklahoma':'OK', 'Oregon':'OR', 'Pennsylvania':'PA', 'Puerto Rico':'PR', 'Rhode Island':'RI',
    'South Carolina':'SC', 'South Dakota':'SD', 'Tennessee':'TN', 'Texas':'TX', 'Utah':'UT',
    'Virginia':'VA', 'Vermont':'VT', 'Washington':'WA', 'Wisconsin':'WI', 'West Virginia':'WV', 'Wyoming':'WY'}
    abb_st = [val for val in dict_states.values()]
    unsolved = df[df["Crime Solved"] != "Yes"]
    # plt.rcParams["figure.figsize"] = (12,4)
    ax = sns.countplot(x="State", hue="Weapon", data=unsolved[unsolved["Weapon"]=="Handgun"])
    ax.set_xticklabels(abb_st)
    plt.title("Unsolved Homicides Caused By Handguns")


    # In[6]:

    ax1 = sns.countplot(x="State", hue="Victim Race", data=unsolved[unsolved["Weapon"]=="Handgun"], palette = "colorblind")
    ax1.set_xticklabels(abb_st)
    ax1.legend(loc = 'upper right')
    plt.title("Unsolved Homicides for different race in various states")
    # sns.palplot(sns.color_palette("colorblind", 10))


    # In[7]:

    ax3 = sns.pairplot( hue="Weapon", data=df[df["Weapon"]=="Handgun"], palette = "colorblind")


    # In[8]:

    ax3 = sns.countplot(x = "Year", hue="Weapon", data=df[df["Weapon"]=="Handgun"], palette = "colorblind")


    # In[ ]:

    ax4 = sns.countplot(x = "Year", hue="Incident", data=df)


# In[21]:




    # In[68]:

    unsolved['Weapon'].value_counts().plot(kind='bar')


    # In[69]:

    unsolved['Year'].value_counts().plot(kind='bar')


    # In[70]:

    rel = unsolved['Weapon'].groupby(unsolved['Victim Sex'])
    rel.size().plot(kind='bar')


    # In[71]:

    unsolved["Month"].value_counts().plot(kind="bar")


# In[47]:


    # In[72]:

    unsolved['Victim Race'].value_counts().plot(kind='bar')

def details():

    df = df = pd.read_csv("crime_dataset.csv", low_memory = False)
    hdata = df[df['Victim Age'] != 998]
    print df["Relationship"].value_counts()

    print

    print "Top 10 Victim ages"
    print hdata["Victim Age"].value_counts()[0:10]

    print
    print df['Weapon'].value_counts()

details()
