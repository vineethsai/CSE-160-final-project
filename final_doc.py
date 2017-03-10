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
from collections import Counter

plt.rcParams["figure.figsize"] = (18, 7)
pylab.rcParams["figure.figsize"] = (18, 7)

def extract_as_list(filename):
    """Opens file, appends each row (as dictionary) into list.

    Parameters:
        filename as string.

    Returns:
        output: list of each row in csv file as a dictionary.
    """

    output = list()
    csv_file = open(filename)
    for row in csv.DictReader(csv_file):
        output.append(row)
    csv_file.close()
    return output

def extract_as_dataframe(filename):
    """Reads in the data of the csv file into DataFrame.

    Parameters:
        filename: filename as string.

    Returns:
        data: DataFrame of csv file.
    """

    data = pd.read_csv(filename, low_memory = False)
    return data

def extract_data_for_months_by_year(data_list):
    """Extracts incidence per month for every year as a dictionary of dictionaries.
    For example, data points for the months of year 1980 would look something like this:

        {1980: {"January" : 18983, "February" : 23213, "March" : 31242 ... etc.}}

    Parameters:
        data_list: list of dictionaries, each item in list is a row of the CSV file.

    Returns:
        output_dict: dictionary mapping year to incidences per month of that year.

    """

    output_dict = dict()

    for row in data_list:
        if row["Year"] in output_dict.keys():
            year_dict = output_dict[row["Year"]]
            if row["Month"] in year_dict.keys():
                output_dict[row["Year"]][row["Month"]] += int(row["Incident"])
            else:
                output_dict[row["Year"]][row["Month"]] = int(row["Incident"])
        else:
            output_dict[row["Year"]] = dict()

    assert (len(output_dict[row["Year"]].keys()) == 12), "Invalid number of months in data file."

    return output_dict

def extract_data_by_categories(data_list, column_names, exclude_points):
    """ Categorizes data points based on which column you want to look at.

    Parameters:
        data_list: list of dictionaries, each item in list is a row of the CSV file.
        column_names: list of column names as strings that you want to investigate.
        exclude_points: list of values as strings that are invalid data points such as "Unknown".

    Returns:
        output_dict: dictionary mapping each column to it's valid data points.
    """

    output_dict = dict()
    # Reading in rows of file, excluding points that are invalid or "placeholder" points
    for row in data_list:
        for name in column_names:
            if row[name] not in exclude_points:
                if name in output_dict.keys():
                    output_dict[name].append(row[name])
                else:
                    output_dict[name] = [row[name]]

    return output_dict

def find_mode_of_category(data_dict, column_name):
    """ Given a specific column name, finds the most common data point (mode) and gives
    its frequency.

    Parameters:
        data_dict: dictionary of selected column names as keys with their data points as values.
        column_name: specific column name to find mode of.

    Returns:
        max_freq_datum: tuple consisting of: (data point that is the mode, frequency of that
        data point).
    """

    data = data_dict[column_name]

    # Finding counts of each data point in column
    number_dict = dict()
    for datum in data:
        if datum in number_dict.keys():
            number_dict[datum] +=  1
        else:
            number_dict[datum] = 1

    # Converting counts into percentage of total data points (frequency)
    num_of_points = sum(number_dict.values())
    for val in number_dict:
        number_dict[val] = float(number_dict[val]) / num_of_points

    # Sorting data from max frequency to min frequency, first datum is max
    max_to_min = sorted(number_dict.items(), key = itemgetter(1), reverse = True)
    max_freq_datum = max_to_min[0]

    return max_freq_datum

def find_max_of_all(data_dict, column_names):
    """ Given multiple column names, finds the modes for each column and their frequencies.

    Parameters:
        data_dict: dictionary of selected column names as keys with their data points as values.
        column_names: list of column names as strings that you want to investigate.

    Returns:
        output: list of tuples, each item in list as a return value from find_mode_of_category.
    """

    output = list()
    for name in column_names:
        max_of_category = find_mode_of_category(data_dict, name)
        output.append(max_of_category)

    return output

def print_max_values(all_maxes, column_names):
    """Formats list returned from find_max_of_all for printing.

    Parameters:
        all_maxes: list returned from find_max_of_all, list of tuples as (mode datum, frequency).
        column_names: list of column names as strings that you want to investigate.

    Returns:
        None, prints results from finding mode of the data.
    """

    for val in range(len(column_names)):
        category = column_names[val]
        max_data = all_maxes[val][0]
        percent = format(float(all_maxes[val][1]) * 100, '.2f')
        print "Most affected %s: %s, %s" % (category, max_data, percent) + "%"

def extract_data_by_state(data_list, column_names, exclude_points, state_name):
    """Gets most modes for chosen columns for chosen state.

    Parameters:
        data_list: list of dictionaries, each item in list is a row of the CSV file.
        column_names: list of column names as strings that you want to investigate.
        exclude_points: list of values as strings that are invalid data points such as "Unknown".
        state_name: state name as string that values are excluded to.

    Returns:
        modes_for_state: list of tuples as returned from find_max_of_all.
    """

    state_list = list()

    # Accumulate relevant rows of data_list for each state to be used to calculate mode
    for row in data_list:
        if row["State"] == state_name:
            state_list.append(row)

    accum_data = extract_data_by_categories(state_list, column_names, exclude_points)
    modes_for_state = find_max_of_all(accum_data, column_names)

    return modes_for_state

def print_state_data(data_list, column_names, exclude_points, states):
    """Formats calculated modes for printing.

    Parameters:
        data_list: list of dictionaries, each item in list is a row of the CSV file.
        column_names: list of column names as strings that you want to investigate.
        exclude_points: list of values as strings that are invalid data points such as "Unknown".
        states: list of states to calculate modes for.

    Returns:
        None, prints values for each state chosen.
    """

    for state in states:
        state_modes = extract_data_by_state(data_list, column_names, exclude_points, state)
        print "For the state of %s:" % (state)
        print_max_values(state_modes, column_names)
        print

def get_user_states(dict_states):
    """Asks user what states they would like to look at, makes sure that it is a valid state.

    Parameters:
        data_dict: dictionary of states mapping to their abbreviations.

    Returns:
        state_list: list of states user selected.
    """

    print "Please capitalize the first letter of the state name."
    state1 = str(raw_input('What is the first state you would like to look at? '))
    state2 = str(raw_input('What is the second state you would like to look at? '))
    print

    state_list = [state1, state2]

    for state in state_list:
        assert (state in dict_states.keys()), "Please type a valid state name!"

    return state_list

def spike_check_visual(year_data):
    """Orders months in chronological order and checks for spikes in total incidents per month.
    
    Parameters: 
        year_data: dictionary of dictionaries, each year mapping to dictionary of months mapping to total incidents.
    
    Returns: 
        None, prints statements.
    """
    year_set = set()
    diff_dict = dict()

    for input_y in range(1980, 2015):
        input_year = str(input_y)
        month_data = year_data[input_year].items()
        x_val = [None] * 12
        y_val = [None] * 12

        # Order the months in chronological order so when graphing, x-axis does not display randomly
        month = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                 "October", "November", "December"]
        for items in month_data:
            for i in range(12):
                if items[0] == month[i]:
                    x_val[i] = items[0]
                    y_val[i] = items[1]

        # Assigning each difference value with what to print if it becomes one of the three largest spikes.
        for i in range(0, 11):
            # A spike is defined as an increase in 125% over the time period of one month.
            if (y_val[i] * 1.25) <= (y_val[i + 1]):         
                year_set.add(input_year)
                diff = y_val[i + 1] - y_val[i]
                diff_dict[diff] = "%s to %s %s" % (x_val[i], x_val[i + 1], input_year)
       
        # Graphing only the years in which there was a spike, for visual confirmation. 
        if input_year in year_set:
            graph_spike_year(x_val, y_val, input_year)


    top_three_diff = sorted(diff_dict.keys())[0:3]
    print "Three largest spikes in total monthly incidents from 1980 to 2014:"
    for diff in top_three_diff:
        print diff_dict[diff]
    print

def graph_spike_year(x_val, y_val, input_year):
    """Graphs each year which has a spike.
    
    Parameters: 
        x_val: list of months.
        y_val: list of total incidents for cooresponding month.
        input_year: string that is the year which we are to graph.
        
    Returns:
        None, saves graph.
    """
    
    pylab.figure(1)
    x = range(12)
    pylab.xticks(x, x_val)
    pylab.plot(x, y_val, "g")
    pylab.title("Number of Incidents per Month for" + input_year)
    pylab.ylabel("Number of Incidents")
    pylab.xlabel("Months")
    pylab.savefig("yearly\incidents_" + str(input_year) + ".png")
    pylab.clf()

def graph_affected_ages(age_clean_data):
    """Graphs plot showing number of incidents for different victim ages.
    
    Parameters:
        age_clean_data: cleaned DataFrame where age is not 998 or 99 (void values)
   
    Returns:
        None, saves graph.
    """

    age_clean_data["Victim Age"].value_counts().sort_index(ascending = True).plot(kind = "bar",
                                                                                color = "purple")
    plt.title("Number of Incidents for all Victim Ages")
    plt.xlabel("Ages")
    plt.ylabel("Number of Incidents")
    plt.savefig("graphs\\victim_age.png")
    plt.clf()

def graph_affected_sexes(data_frame):
    """Graphs plot showing number of incidents for different victim sexes.
   
    Parameters:
        data_frame: DataFrame of csv file.
   
    Returns:
        None, saves graph.
    """

    data_frame["Victim Sex"].value_counts().plot(kind = 'bar')
    plt.title("Number of Incidents for Victim Sexes")
    plt.ylabel("Number of Incidents")
    plt.savefig("graphs\\number_hom_sex.png")
    plt.clf()

def graph_affected_races(data_frame):
    """Graphs plot showing number of incidents for different victim races.
    
    Parameters:
        data_frame: DataFrame of csv file.
    
    Returns:
        None, saves graph.
    """

    ax1 = sns.countplot(x = "Victim Race", hue = "Victim Race", data = data_frame, palette = 
    "colorblind")
    ax1.legend(loc = 'upper right')
    plt.title("Number of Incidents for Victim Races")
    plt.xlabel("Victim Races")
    plt.ylabel("Number of Incidents")
    plt.savefig("graphs\unsolved_hom_race_state.png")
    plt.clf()

def graph_affected_race_for_state(data_frame, dict_states):
    """For each state, graphs victim race.
    
    Parameters:
        data_frame: DataFrame of csv file.
        dict_states: dictionary of all states
    
    Returns:
        None, saves graph.
    """

    abb_st = [val for val in dict_states.values()]

    ax6 = sns.countplot(x = "State", hue = "Victim Race", data = data_frame, palette = 
    "colorblind")
    ax6.set_xticklabels(abb_st)
    ax6.legend(loc = 'upper right')
    plt.title("Frequency of Victim Race Based on State")
    plt.ylabel("Number of Incidents")
    plt.savefig("graphs\hom_race_state.png")
    plt.clf()

def graph_weapons_handgun_over_time(data_frame):
    """Graphs number of cases with weapon documented as "handgun". Graphs handgun use over time.
    
    Parameters:
        data_frame: DataFrame of csv file.
    
    Returns:
        None, saves graph.
    """
    
    ax2 = sns.countplot(x = "Year", hue = "Weapon", data = data_frame[data_frame["Weapon"] == "Handgun"],
                        palette = "colorblind")
    ax2.legend(loc = 'upper right')
    plt.title("Use of Handguns over Time")
    plt.xlabel("Years")
    plt.ylabel("Number of Homicides using Handguns")
    plt.savefig("graphs\handgun_time.png")
    plt.clf()
    
def find_incidents_for_states(data_list):
    """Finds total number of incidents per state.
    
    Parameters: 
        data_list: list of dictionaries, each item in list is a row of the CSV file.
        
    Returns: 
        state_dict: dictionary mapping each state to it's total number of incidents.
    """
    
    state_dict = dict()
    
    for row in data_list: 
        if row["State"] in state_dict.keys():
            state_dict[row["State"]] += int(row["Incident"])
        else:
            state_dict[row["State"]] = int(row["Incident"])
            
    return state_dict
        
def graph_crime_state(data_frame, dict_states):
    """Graphs total incidents for each state. 
    
    Parameters: 
        dict_states: dictionary of states mapping to their abbreviation.
        data_frame: DataFrame of csv file.
        
    Returns: 
        None, saves graph.
    """
    
    states = dict(Counter(data_frame[data_frame["Weapon"] == "Handgun"]["State"].values))
    abb_st = [val for val in dict_states.values()]
    ax70 = sns.countplot(x = "State", hue = "Weapon", data = data_frame)
    ax70.set_xticklabels(abb_st)
    ax70.legend_.remove()
    plt.title("Frequency of Incidents in all State")
    plt.ylabel("Number of Incidents")
    plt.savefig("graphs\incidents_state.png")
    plt.clf()

def main():
    """ Will run main program when final_doc.py is run """

    print "Welcome to Nanda and Vineeth's data analysis for all US homicides from 1980 - 2014"
    print "Our data set has more than 600,000 data points, so please bear with us if the program is slow"
    print
    
    filename = "crime_data.csv"
    column_names = ["Victim Sex", "Victim Age", "Victim Race", "Relationship"]
    exclude_points = ["Unknown", "0", "998"]

    dict_states = {
        "Alaska": "AK", "Alabama": "AL", "Arkansas": "AR", "Arizona": "AZ", "California": "CA", "Colorado": "CO",
        "Connecticut": "CT", "District of Columbia": "DC", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
        "Hawaii": "HI", "Iowa": "IA", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Kansas": "KS","Kentucky": "KY",
        "Louisiana": "LA", "Massachusetts": "MA", "Maryland": "MD", "Maine": "ME", "Michigan": "MI",
        "Minnesota": "MN", "Missouri": "MO", "Mississippi": "MS", "Montana": "MT", "North Carolina": "NC",
        "North Dakota": "ND", "Nebraska": "NE", "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM",
        "Nevada": "NV", "New York": "NY", "Ohio": "OH", "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
        "Puerto Rico": "PR", "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD", "Tennessee": "TN",
        "Texas": "TX", "Utah": "UT", "Virginia": "VA", "Vermont": "VT", "Washington": "WA", "Wisconsin": "WI",
        "West Virginia": "WV", "Wyoming": "WY"
    }

    # Extract data from CSV file
    data_list = extract_as_list(filename)

    # Find all data points for victim sex, race, age, and relationship
    data_dict = extract_data_by_categories(data_list, column_names, exclude_points)
    
    # Compare two state modes based on user input
    answer = str(raw_input("Would you like to compare modes for two states? (yes/no) "))
    print
    if answer.lower() == "yes":
        states = get_user_states(dict_states)
        print_state_data(data_list, column_names, exclude_points, states)
    else:
        print "Please wait for the remaining computations!"
        print

    # Find most common datum for victim sex, race, age, and relationship
    all_maxes = find_max_of_all(data_dict, column_names)
    print "For all states:"
    print_max_values(all_maxes, column_names)
    print

    print "Please wait, the program is graphing the results"
    print

    # Find incidence rate per month for every year
    year_data = extract_data_for_months_by_year(data_list)
    spike_check_visual(year_data)

    # Extract data from CSV file as DataFrame
    data_frame = extract_as_dataframe(filename)

    # Graph affected victim ages
    age_clean_data = data_frame[data_frame["Victim Age"] !=  998]
    age_clean_data = age_clean_data[age_clean_data["Victim Age"] !=  99]
    graph_affected_ages(age_clean_data)

    # Graph use of handguns over time
    graph_weapons_handgun_over_time(data_frame)

    # Graph affected victim sex based on frequency
    graph_affected_sexes(data_frame)

    # Graph affected victim races based on frequency
    graph_affected_races(data_frame)

    # Graph affected victim races based on frequency per state
    graph_affected_race_for_state(data_frame, dict_states)

    # Graph all incidents for all states
    graph_crime_state(data_frame, dict_states)

    print "Check the folder 'yearly' and 'graphs' for the graphs"
    print
    print "Done"

if __name__ == "__main__":
    main()
