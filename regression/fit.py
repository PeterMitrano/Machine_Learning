#!/usr/bin/python

# This script takes in a bunch of points in 2 dimensions (x,y)
# and fits a polynomial of a degree somewhere between 0 and MAX_DEGREE.
# It folds the data and uses cross validation.

import warnings
import sys
import numpy as np
import matplotlib.pyplot as plt

warnings.simplefilter('ignore', np.RankWarning)

MAX_DEGREE = 12
k = 4

all_data = np.array([
    [0, -10],
    [1, -6],
    [4, -2],
    [5, 2],
    [6, 4],
    [7, 6],
    [9, 5],
    [10, 7],
    [14, 7],
    [15, 5],
    [16, 4],
    [18, 3],
    [20, 0],
    [21, -5],])

def compute_best_coefficients(all_data):
    # split data into test & validation.
    # keep (n - n/k) and test on n/k.
    n = all_data.shape[0]

    lowest_error = 10000
    average_errors = []

    all_x = [i[0] for i in all_data]
    all_y = [i[1] for i in all_data]
    max_x_in_data = max(all_x)
    min_x_in_data = min(all_x)
    max_y_in_data = max(all_y)
    min_y_in_data = min(all_y)
    print min_x_in_data, max_x_in_data

    reg_axes = plt.subplot(211)

    for degree in range(MAX_DEGREE):
        start = 0
        end = n/k
        error = 0
        sum_mean_sqrd_error = 0

        while end < n:
            current_test_x = []
            current_test_y = []

            # setup input lists
            # we leave out all data between start and end.
            for i in range(0,start):
                current_test_x.append(all_data[i][0])
                current_test_y.append(all_data[i][1])

            for i in range(end,n):
                current_test_x.append(all_data[i][0])
                current_test_y.append(all_data[i][1])

            # do the regression!
            regression_func = np.poly1d(np.polyfit(current_test_x, current_test_y, degree))

            # now we test on the validation set
            for i in range(start, end):
                prediction = regression_func(all_data[i][0])
                error += (prediction - all_data[i][1])**2

            sum_mean_sqrd_error += error / (end - start)

            start += 1
            end += 1

        average_error = sum_mean_sqrd_error / ( n - (n / k))
        average_errors.append(average_error)

        print "avg error for degree " + str(degree) + " is " + str(average_error)

        # this is a regression of all the data, and isn't actually used in any math
        # it's just for showing how good the fit is generally speaking
        regression_func_for_degree = np.poly1d(np.polyfit(all_x, all_y, degree))
        x_range = np.linspace(min_x_in_data, max_x_in_data, 100)
        plt.plot(x_range, regression_func_for_degree(x_range))

        if average_error < lowest_error:
            lowest_error = average_error
            best_func = regression_func

    plt.plot(all_x, all_y, 'g.')
    reg_axes.set_xlim(min_x_in_data, max_x_in_data)
    reg_axes.set_ylim(min_y_in_data, max_y_in_data)

    avg_err_axes = plt.subplot(212)
    avg_err_axes.set_ylim([0, 1000])
    plt.plot(average_errors)
    plt.show()

def graph_data_and_best_fit(coefficients):
    pass

if __name__ == '__main__':
    coefficients = compute_best_coefficients(all_data)
    graph_data_and_best_fit(coefficients)
    print all_data.shape
