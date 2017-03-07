
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams["figure.figsize"] = (18,7)
import csv 
from operator import itemgetter

df = pd.read_csv("crime_dataset.csv", low_memory=False)
hdata = df[df['Victim Age']!=998]
unsolved = df[df["Crime Solved"] != "Yes"]
dict_states = {'Alaska': 'AK', 'Alabama': 'AL', 'Arkansas': 'AR', 'Arizona': 'AZ',
               'California': 'CA', 'Colorado': 'CO',
               'Connecticut': 'CT',
               'District of Columbia': 'DC', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
               'Hawaii': 'HI',
               'Iowa': 'IA',
               'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Kansas': 'KS', 'Kentucky':
	               'KY',  'Louisiana': 'LA',
               'Massachusetts': 'MA', 'Maryland': 'MD', 'Maine': 'ME', 'Michigan': 'MI',
               'Minnesota': 'MN',
               'Missouri': 'MO',
               'Mississippi': 'MS', 'Montana': 'MT', 'North Carolina': 'NC', 'North Dakota':
	               'ND',  'Nebraska': 'NE',
               'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'Nevada': 'NV',
               'New York': 'NY',
               'Ohio': 'OH',
               'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Puerto Rico': 'PR',
               'Rhode Island': 'RI',
               'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX',
               'Utah': 'UT',
               'Virginia': 'VA', 'Vermont': 'VT', 'Washington': 'WA', 'Wisconsin': 'WI',
               'West Virginia': 'WV',
               'Wyoming': 'WY'}
abb_st = [val for val in dict_states.values()]
unsolved_handgun = unsolved[unsolved["Weapon"] == "Handgun"]
handgun = df[df["Weapon"] == "Handgun"]

def visual():

    # Deaths Attributable to Various Weapons
    df["Weapon"].value_counts().plot(kind = "bar", color = "LightGreen")
    plt.title('Deaths Attributed to Various Weapons')
    plt.savefig("weapons.png")
    plt.clf()

    # Graph showing number of incidents for different Victim Ages
    hdata["Victim Age"].value_counts().sort_index(ascending = True).plot(kind = "bar",
                                                                        color = "purple")
    plt.title('Graph showing number of incidents for different Victim Ages')
    plt.savefig("victim_age.png")
    plt.clf()

    # Number of Unsolved Homicides: 1980 to 2014
    unsolved['Year'].value_counts().sort_index(ascending = True).plot(kind = 'line', color = "Red")
    plt.title('Number of Unsolved Homicides: 1980 to 2014')
    plt.savefig("unsolved_hom.png")
    plt.clf()

    # Unsolved Homicides Caused By Handguns
    ax = sns.countplot(x = "State", hue = "Weapon", data = unsolved_handgun,  palette =
    "colorblind")
    ax.set_xticklabels(abb_st)
    plt.title("Unsolved Homicides Caused By Handguns")
    plt.savefig("unsolved_hom_handgun.png")
    plt.clf()

    # Bar graph of unsolved homicides for various weapons

    unsolved['Weapon'].value_counts().plot(kind='bar')
    plt.title("Bar graph of unsolved homicides for various weapons")
    plt.savefig("unsolved_weapon.png")
    plt.clf()

    # Bar graph of unsolved cases per year to count

    unsolved['Year'].value_counts().plot(kind='bar')
    plt.title("Bar graph of unsolved cases per year to count")
    plt.savefig("unsolved_year.png")
    plt.clf()

    # Bar graph of unsolved cases victim sex to the type of weapon used

    rel = unsolved['Weapon'].groupby(unsolved['Victim Sex'])
    rel.size().plot(kind='bar')
    plt.title("Bar graph of unsolved cases victim sex to the type of weapon used")
    plt.savefig("unsolved_weapon_sex.png")
    plt.clf()

    # Bar graph of unsolved cases for various victim races to the month of incident

    unsolved["Month"].value_counts().plot(kind="bar")
    plt.title("Bar graph of unsolved cases for various victim races to the month of incident")
    plt.savefig("unsolved_month.png")
    plt.clf()

    # Plot of number of unsolved incidents for various victim races

    unsolved['Victim Race'].value_counts().plot(kind='bar')
    plt.title("Bar graph of unsolved cases for various victim races to number of incidents")
    plt.savefig("unsolved_race.png")
    plt.clf()


    # Unsolved Homicides for different race in various states

    ax1 = sns.countplot(x = "State", hue = "Victim Race", data = unsolved_handgun, palette =
    "colorblind")
    ax1.set_xticklabels(abb_st)
    ax1.legend(loc = 'upper right')
    plt.title("Unsolved Homicides for different race in various states")
    plt.savefig("unsolved_hom_race_state.png")
    plt.clf()


    # Graph of use of handguns over time

    ax2 = sns.countplot(x = "Year", hue = "Weapon", data = df[df["Weapon"]=="Handgun"], palette =
    "colorblind")
    ax2.legend(loc = 'upper right')
    plt.title("graph of use of handguns over time")
    plt.savefig("handgun_time.png")
    plt.clf()


    # Plot shows number of incidents over time

    ax3 = sns.countplot(x = "Year", hue = "Incident", data=df)
    ax3.legend_.remove()
    plt.title("Plot shows number of incidents over time")
    plt.savefig("incidents_time.png")
    plt.clf()




def details():


    relationship = df[df["Relationship"]!= "Unknown"]
    vic_age = df[df['Victim Age'] != 998]
    print "Number of Incidents for different types of relationships"
    print relationship["Relationship"].value_counts()

    print

    print "Top 10 Victim ages"
    print vic_age["Victim Age"].value_counts()[0:10]

    print

    print "Number of Incidents for different types of Weapons"
    print df['Weapon'].value_counts()

def get_plot():

    user_plot = raw_input("which year do you want your plot to show? ")
    plot_data =  df[df["Year"] == int(user_plot)]
    # ax4 = sns.countplot(x="Month", hue ="Incident", data = plot_data)
    plot_data.sort_index(ascending = True).plot(kind="bar",x = "Month",  y = "Incident", color="purple")
    plt.savefig("user_input_2.png")
    plt.show()

get_plot()
visual()
details()
