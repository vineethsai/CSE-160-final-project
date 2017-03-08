# Name: Nanda Sundaresan
# UW NetID: nandas
# Name: Vineeth Sai Narajala
# UW NetID: vineeth7
# CSE 160

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import csv
from operator import itemgetter

plt.rcParams["figure.figsize"] = (18, 7)


def get_data(filename):
    data = pd.read_csv(filename, low_memory=False)
    return data

def graph_affected_ages(hdata):
    # Graph showing number of incidents for different Victim Ages

    hdata["Victim Age"].value_counts().sort_index(ascending=True).plot(kind="bar", color="purple")
    plt.title('Graph showing number of incidents for different Victim Ages')
    plt.savefig("victim_age.png")
    plt.clf()

def graph_affected_sexes():
    pass

def graph_affected_races():
    pass

def graph_total_incidence_for_year(year, data):
    """Takes input of year, plots graph of number of incidences of
    homicide per month for that year. Returns none."""
    assert (int(year) >= 1980 and int(year) <= 2014), "Please choose a year inside the range of the data!"

    plot_data = data[data["Year"] == int(year)]
    plot_data["Month"].value_counts().sort_index(ascending=True).plot(kind="bar", color="purple")
    plt.savefig("user_input_2.png")
    print "***Graph plotted, please close graph window to continue***"
    plt.show()

def graph_affected_race_for_month():
    """input month and year and it'll show you a bar graph of
    affected races in that month, we can see if there is an increase
    in crimes against a specific race in the month with the spike"""
    pass

def graph_weapons_over_time():
    # Graph of use of handguns over time
    ax2 = sns.countplot(x="Year", hue="Weapon", data=df[df["Weapon"] == "Handgun"], palette=
    "colorblind")
    ax2.legend(loc='upper right')
    plt.title("graph of use of handguns over time")
    plt.savefig("handgun_time.png")
    plt.clf()

def main():
    data = get_data("crime_dataset.csv")

    # Graph incidences over every month in a chosen year
    year = raw_input("Which year do you want your plot to show? ")
    graph_total_incidence_for_year(year, data)

    # Graph affected victim ages
    hdata = data[data['Victim Age'] != 998]
    graph_affected_ages(hdata)

    # Prints three most affected relationships between perp. and victim.
    relationship = data[data["Relationship"] != "Unknown"]
    print "Number of Incidents for different types of relationships"
    print relationship["Relationship"].value_counts()[0:3]
    print

    # Prints three most affected victim ages
    vic_age = data[data['Victim Age'] != 998]
    print "Top 3 Victim ages"
    print vic_age["Victim Age"].value_counts()[0:3]
    print

    # print "Number of Incidents for different types of Weapons"
    # print data['Weapon'].value_counts()

if __name__ == "__main__":
    main()















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

