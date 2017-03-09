# Name: Nanda Sundaresan
# UW NetID (Nanda Sundaresan): nandas
# UW NetID (Vineeth Sai Narajala): vineeth7
# CSE 160
# Homework 7: Final project

import csv
from operator import itemgetter
import matplotlib.pyplot as plt
import pylab
import pandas as pd
import seaborn as sns

plt.rcParams["figure.figsize"] = (18, 7)
pylab.rcParams["figure.figsize"] = (18, 7)

def extract_as_list(filename):
    """ Opens file, appends each row (as dictionary) into list"""
    output = list()
    csv_file = open(filename)
    for row in csv.DictReader(csv_file):
        output.append(row)
    return output

def extract_as_dataframe(filename):
    """
    reads in the data
    :param filename: name of the csv file
    :return: reads the data as a data frame
    """
    data = pd.read_csv(filename, low_memory=False)
    return data
def extract_data_for_months_by_year(data_list):
    """Extracts incidence per month for every year, dictionary of dictionaries"""
    output_dict = dict()
    for row in data_list:
        # print row
        if row['Year'] in output_dict.keys():
            year_dict = output_dict[row["Year"]]
            if row["Month"] in year_dict.keys():
                output_dict[row["Year"]][row["Month"]] += int(row["Incident"])
            else:
                output_dict[row["Year"]][row["Month"]] = int(row["Incident"])
        else:
            output_dict[row["Year"]] = dict()
    return output_dict
                
def extract_data_by_categories(data_list, column_names, exclude_points):
    """ Categorizes data points based on which column data you want to look at"""
    output_dict = dict()
    # Reading each row of the csv file, excluding points that are invalid or
    # "placeholder" points
    for row in data_list:
        for name in column_names:
            if row[name] not in exclude_points:
                if name in output_dict.keys():
                    output_dict[name].append(row[name])
                else:
                    output_dict[name] = [row[name]]

    return output_dict



def find_mode_of_category(data_dict, column_name):
    """ Finds the most common value in that category """

    data = data_dict[column_name]

    # Finding counts of each data point in column
    number_dict = dict()
    for datum in data:
        if datum in number_dict.keys():
            number_dict[datum] += 1
        else:
            number_dict[datum] = 1

    # Converting counts into percentage of total data points
    num_of_points = sum(number_dict.values())
    for val in number_dict:
        number_dict[val] = float(number_dict[val]) / num_of_points

    # Sorting data from max frequency to min frequency, first datum is max
    max_to_min = sorted(number_dict.items(), key=itemgetter(1), reverse=True)
    max_freq_datum = max_to_min[0]

    return max_freq_datum


def find_max_of_all(data_dict, column_names):
    """ Formats modes into list """

    output = list()
    for name in column_names:
        max_of_category = find_mode_of_category(data_dict, name)
        output.append(max_of_category)

    return output
    
def print_max_values(all_maxes, column_names):
    """Formats find_max_of_all for printing"""
    
    for val in range(len(column_names)):
        category = column_names[val]
        max_data = all_maxes[val][0]
        percent = format(float(all_maxes[val][1]) * 100, '.2f')
        print "Most affected %s: %s, %s" % (category, max_data, percent) + "%"

def spike_check_visual(year_data):
    """
    :param year_data:
    :return:
    """
    for input_y in range(1980,2015):
        input_year = str(input_y)
        item = year_data[input_year].items()
        x_val = [None]*12
        y_val = [None]*12

        for items in item:
            if items[0] == "January":
                x_val[0]= items[0]
                y_val[0]= items[1]
            elif items[0] == 'February':
                x_val[1] = items[0]
                y_val[1] = items[1]
            elif items[0] == 'March':
                x_val[2] = items[0]
                y_val[2] = items[1]
            elif items[0] == 'April':
                x_val[3] = items[0]
                y_val[3] = items[1]
            elif items[0] == 'May':
                x_val[4] = items[0]
                y_val[4] = items[1]
            elif items[0] == 'June':
                x_val[5] = items[0]
                y_val[5] = items[1]
            elif items[0] == 'July':
                x_val[6] = items[0]
                y_val[6] = items[1]
            elif items[0] == 'August':
                x_val[7] = items[0]
                y_val[7] = items[1]
            elif items[0] == 'September':
                x_val[8] = items[0]
                y_val[8] = items[1]
            elif items[0] == 'October':
                x_val[9] = items[0]
                y_val[9] = items[1]
            elif items[0] == 'November':
                x_val[10] = items[0]
                y_val[10] = items[1]
            else:
                x_val[11] = items[0]
                y_val[11] = items[1]

        for i in range(0,11):
            if (y_val[i]*1.27) <= (y_val[i+1]):
                print "There is a spike from ", x_val[i],"to", x_val[1+i], input_year

        pylab.clf()
        pylab.figure(1)
        x = range(12)
        pylab.xticks(x, x_val)
        pylab.plot(x, y_val, "g")
        pylab.title("Graph showing number of incidents per month for the year "+input_year)
        pylab.ylabel("Number of Incidents")
        pylab.xlabel("Months")
        pylab.savefig("yearly\incidents_"+ str(input_year)+".png")



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
    ax2 = sns.countplot(x="Year", hue="Weapon", data=data_frame[data_frame["Weapon"] == "Handgun"], 
                        palette="colorblind")
    ax2.legend(loc='upper right')
    plt.title("graph of use of handguns over time")
    plt.savefig("graphs\handgun_time.png")
    plt.clf()

def main():
    """ Will run main program when final_doc.py is run """

    filename = "crime_data.csv"
    column_names = ["Victim Sex", "Victim Age", "Victim Race", "Relationship"]
    exclude_points = ['Unknown', '0', '998']

    # Extracts CSV file into list
    data_list = extract_as_list(filename)
    # Combines all values for given columns
    data_dict = extract_data_by_categories(data_list, column_names, exclude_points)
    # Finds modes of each column selected
    all_maxes = find_max_of_all(data_dict, column_names)
    
    print_max_values(all_maxes, column_names)

    # Find incidence rate per month for every year
    year_data = extract_data_for_months_by_year(data_list)
    spike_check_visual(year_data)

    data_frame = extract_as_dataframe(filename)

    # Graph affected victim ages
    age_clean_data = data_frame[data_frame['Victim Age'] != 998]
    age_clean_data = age_clean_data[age_clean_data['Victim Age'] != 99]
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