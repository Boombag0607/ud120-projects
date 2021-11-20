#!/usr/bin/python3
import numpy as np
import joblib
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
#outlier removal
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)


### your code below 
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


#outlier finder
# for key, value in data_dict.items():
#     if value['bonus'] == data.max():
#         print(key)

#more outliers
for key, value in data_dict.items():
    if value['salary'] != 'NaN' and value['bonus'] !=  'NaN':
        if int(value['salary']) > 1000000 and int(value['bonus']) > 5000000:
            print(key)
    