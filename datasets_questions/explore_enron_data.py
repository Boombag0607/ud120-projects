#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import joblib

enron_data = joblib.load(open("../final_project/final_project_dataset.pkl", "rb"))

#print(len(enron_data))
#print(len(enron_data["SKILLING JEFFREY K"]))

## counting the number of 'person of interest' in the enron data
# num = 0
# for person in enron_data:
#     if enron_data[person]['poi'] == 1:
#         num = num + 1
# print(num)

## counting the total number of 'person of interest'
# enron_names = open('../final_project/poi_names.txt', 'r')
# for line in enron_names:
#     if '(y)' or '(n)' in line:
#         num = num + 1

# print(num)

## data from James Prentice
## data from Colwell Wesley
## data from Jeffrey K. Skillling
# print(enron_data['SKILLING JEFFREY K'])