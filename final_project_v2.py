# Name: Nanda Sundaresan
# UW NetID (Nanda Sundaresan): nandas
# UW NetID (Vineeth Sai Narajala): vineeth7
# CSE 160
# Homework 7: Final project

import csv
from operator import itemgetter


def extract_rows(filename):
    """ Opens file, appends each row (as dictionary) into list"""

    output = list()
    csv_file = open(filename)

    for row in csv.DictReader(csv_file):
        output.append(row)
    return output

def extract_data_by_cat(data_list, years):
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

def extract_data_by_state(data_list, column_names, exclude_points):
    output_dict = dict()

    for row in data_list:
        extract_category_data = extract_data_by_categories(data_list, column_names, exclude_points)
        if row["State"] in output_dict.keys():
            output_dict[row["State"]].append(extract_category_data)
        else:
            output_dict[row["State"]] = [extract_category_data]
    
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

def state_max_data(states_data, column_names):
    output = list()
    
    for state in states_data.keys():
        print state + ":"
        max_data_state = find_max_of_all(states_data[state][0], column_names)
        output.append(max_data_state)
        
    
    return output
    
def main():
    """ Will run main program when final_project.py is run """

    filename = "crime_data.csv"
    column_names = ["Victim Sex", "Victim Age", "Victim Race", "Relationship"]
    years = range(1980, 2015)
    exclude_points = ['Unknown', '0', '998']
    
   
    data_list = extract_rows(filename)
    data_dict = extract_data_by_categories(data_list, column_names, exclude_points)
    
    year_data =  extract_data_by_cat(data_list, years)
    assert len(year_data.keys()) == len(years)

    #all_maxes = find_max_of_all(data_dict, column_names)
    #print_max_values (all_maxes, column_names)
    
    #states_data = extract_data_by_state(data_list, column_names, exclude_points)
    #print states_data["California"][0]
    #print state_max_data(states_data, column_names)
    
    
    
    
if __name__ == "__main__":
    main()
