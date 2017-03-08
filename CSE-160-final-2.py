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


def get_data_as_df(filename):
    """
    reads in the data
    :param filename: name of the csv file
    :return: reads the data as a data frame
    """
    data = pd.read_csv(filename, low_memory=False)
    return data

def graph_affected_ages(age_clean_data):
    """
    Graph showing number of incidents for different Victim Ages
    :param age_clean_data: cleaned data frame where age != 998 or 99
    :return: None
    :Side effects: Saves graph of affected ages
    """

    age_clean_data["Victim Age"].value_counts().sort_index(ascending=True).plot(kind="bar", color="purple")
    plt.title('Graph showing number of incidents for different Victim Ages')
    plt.savefig("graphs\\victim_age.png")
    plt.clf()

def graph_affected_sexes(data_frame):
    """
    graphs the affected sexes
    :param data_frame: data frame to be graphed
    :return: None
    :side effects: Saves graph of affected sexes
    """

    data_frame['Victim Sex'].value_counts().plot(kind='bar')
    plt.title("Bar graph of victim sexes to number of incidents")
    plt.savefig("graphs\\number_hom_sex.png")
    plt.clf()

def graph_affected_races(data_frame):
    """
    graphs the effected races
    :param data_frame: data frame to be graphed
    :return: None
    :side effects: Saves graph of affected races
    """
    ax1 = sns.countplot(x="Victim Race", hue="Victim Race", data=data_frame, palette=
    "colorblind")
    ax1.legend(loc='upper right')
    # data_frame['Victim Race'].value_counts().plot(kind='bar')
    plt.title("Count of Homicides for different race ")
    plt.savefig("graphs\unsolved_hom_race_state.png")
    plt.clf()


def graph_affected_race_for_state(data_frame):
    """
    input month and year and it'll show you a bar graph of
    affected races in that month, we can see if there is an increase
    in crimes against a specific race in the month with the spike
    :param data_frame: data frame to be graphed
    :return:None
    """
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

    ax6 = sns.countplot(x="State", hue="Victim Race", data=data_frame, palette=
    "colorblind")
    ax6.set_xticklabels(abb_st)
    ax6.legend(loc='upper right')
    plt.title("Homicides for different race in various states")
    plt.savefig("graphs\hom_race_state.png")
    plt.clf()

def graph_weapons_handgun_over_time(data_frame):
    """
    Graph of use of handguns over time
    :return: None
    :side effect: save a graph showing use of handguns over time
    """

    ax2 = sns.countplot(x="Year", hue="Weapon", data=data_frame[data_frame["Weapon"] == "Handgun" ], palette=
    "colorblind")
    ax2.legend(loc='upper right')
    plt.title("graph of use of handguns over time")
    plt.savefig("graphs\handgun_time.png")
    plt.clf()

def main():

    data_frame = get_data_as_df("crime_dataset.csv")


    # Graph affected victim ages
    age_clean_data = data_frame[data_frame['Victim Age'] != 998]
    age_clean_data=age_clean_data[age_clean_data['Victim Age'] != 99]
    graph_affected_ages(age_clean_data)

    # graphs weapon over time
    graph_weapons_handgun_over_time(data_frame)

    # graphs affected sex
    graph_affected_sexes(data_frame)

    # graphs affected races
    graph_affected_races(data_frame)

    graph_affected_race_for_state(data_frame)

if __name__ == "__main__":
    main()




