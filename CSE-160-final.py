












"""
    unsolved = data[data["Crime Solved"] != "Yes"]

    dict_states = {
        'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'Arizona': 'AZ', 'California': 'CA', 'Colorado': 'CO',
        'Connecticut': 'CT', 'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
        'Hawaii': 'HI', 'Iowa': 'IA', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA', 'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI',
        'Minnesota': 'MN', 'Missouri': 'MO', 'Mississippi': 'MS', 'Montana': 'MT', 'North Carolina': 'NC',
        'North Dakota': 'ND', 'Nebraska': 'NE', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
        'Nevada': 'NV', 'New York': 'NY', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
        'Puerto Rico': 'PR', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
        'Texas': 'TX', 'Utah': 'UT', 'Virginia': 'VA', 'Vermont': 'VT', 'Washington': 'WA', 'Wisconsin': 'WI',
        'West Virginia': 'WV', 'Wyoming': 'WY'
    }

    abb_st = [val for val in dict_states.values()]
    unsolved_handgun = unsolved[unsolved["Weapon"] == "Handgun"]
    handgun = data[data["Weapon"] == "Handgun"]
"""

"""___________________________________________________________________________________________________________"""

"""
    # Deaths Attributable to Various Weapons
    df["Weapon"].value_counts().plot(kind = "bar", color = "LightGreen")
    plt.title('Deaths Attributed to Various Weapons')
    plt.savefig("weapons.png")
    plt.clf()
"""

"""
    # Plot shows number of incidents over time
    ax3 = sns.countplot(x = "Year", hue = "Incident", data=df)
    ax3.legend_.remove()
    plt.title("Plot shows number of incidents over time")
    plt.savefig("incidents_time.png")
    plt.clf()
"""

"""
    # Number of Unsolved Homicides: 1980 to 2014
    unsolved['Year'].value_counts().sort_index(ascending = True).plot(kind = 'line', color = "Red")
    plt.title('Number of Unsolved Homicides: 1980 to 2014')
    plt.savefig("unsolved_hom.png")
    plt.clf()
"""

"""
    # Unsolved Homicides Caused By Handguns
    ax = sns.countplot(x = "State", hue = "Weapon", data = unsolved_handgun,  palette =
    "colorblind")
    ax.set_xticklabels(abb_st)
    plt.title("Unsolved Homicides Caused By Handguns")
    plt.savefig("unsolved_hom_handgun.png")
    plt.clf()
"""

"""
    # Bar graph of unsolved homicides for various weapons
    unsolved['Weapon'].value_counts().plot(kind='bar')
    plt.title("Bar graph of unsolved homicides for various weapons")
    plt.savefig("unsolved_weapon.png")
    plt.clf()
"""

"""
    # Bar graph of unsolved cases per year to count
    unsolved['Year'].value_counts().plot(kind='bar')
    plt.title("Bar graph of unsolved cases per year to count")
    plt.savefig("unsolved_year.png")
    plt.clf()
"""

"""
    # Bar graph of unsolved cases victim sex to the type of weapon used
    rel = unsolved['Weapon'].groupby(unsolved['Victim Sex'])
    rel.size().plot(kind='bar')
    plt.title("Bar graph of unsolved cases victim sex to the type of weapon used")
    plt.savefig("unsolved_weapon_sex.png")
    plt.clf()
"""

"""
    # Bar graph of unsolved cases for various victim races to the month of incident
    unsolved["Month"].value_counts().plot(kind="bar")
    plt.title("Bar graph of unsolved cases for various victim races to the month of incident")
    plt.savefig("unsolved_month.png")
    plt.clf()
"""

"""
    # Plot of number of unsolved incidents for various victim races
    unsolved['Victim Race'].value_counts().plot(kind='bar')
    plt.title("Bar graph of unsolved cases for various victim races to number of incidents")
    plt.savefig("unsolved_race.png")
    plt.clf()
"""

"""
    # Unsolved Homicides for different race in various states
    ax1 = sns.countplot(x = "State", hue = "Victim Race", data = unsolved_handgun, palette =
    "colorblind")
    ax1.set_xticklabels(abb_st)
    ax1.legend(loc = 'upper right')
    plt.title("Unsolved Homicides for different race in various states")
    plt.savefig("unsolved_hom_race_state.png")
    plt.clf()
"""
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
# plt.show()


# In[ ]:



