#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn.svm import SVC

features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]

clf = SVC(kernel = 'rbf', gamma='auto')

t0 = time()
clf.fit(features_train, labels_train)
print('Training Time:', round(time()-t0, 3), 's')

t0 = time()
pred = clf.predict(features_test)
print('Predicting Time:', round(time()-t0, 3), 's')

from sklearn.metrics import accuracy_score

acc = accuracy_score(pred, labels_test)
print(acc)

#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''
# No. of Chris training emails :  7936
# No. of Sara training emails :  7884
# Training Time: 0.024 s
# Predicting Time: 0.364 s
# 0.8953356086461889

#########################################################
