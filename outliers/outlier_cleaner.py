#!/usr/bin/python3

import pandas as pd
import math


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    # original_len = len(net_worths)
    # outlier_detect = list()

    # # your code goes here
    # new_net_worths = []
    # new_ages = []
    # import numpy as np
    # for i in range(len(predictions)):
    #     outlier_detect.append(abs(predictions[i, 0] - net_worths[i, 0]))
    # print(outlier_detect)
    # while(len(new_net_worths) > 0.9*original_len):
    #     idx = outlier_detect.index(max(outlier_detect))
    #     outlier_detect.remove(max(outlier_detect))
    #     # new_predictions = np.delete(predictions, idx, axis=0)
    #     # predictions = new_predictions
    #     new_net_worths = np.delete(net_worths, idx, axis=0)
    #     net_worths = new_net_worths
    #     new_ages = np.delete(ages, idx, axis=0)
    #     ages = new_ages
    # print(max(outlier_detect))

    # for i in range(len(predictions)):
    #     cleaned_data.append((ages[i, 0], net_worths[i, 0], outlier_detect[i]))

    res = zip(predictions, ages, net_worths)

    res_df = pd.DataFrame(res, columns=['predictions', 'ages', 'net_worths'])

    res_df['errors'] = abs(res_df['predictions'] - res_df['net_worths'])

    res_sorted = res_df.sort_values(by='errors', ascending=True)

    res_cleaned = res_sorted.head(81)

    cleaned_data = list(
        zip(res_cleaned['ages'], res_cleaned['net_worths'], res_cleaned['errors']))
    return cleaned_data
