#!/usr/bin/python

# This script takes in a bunch of points in 2 dimensions (x,y)
# and fits a polynomial of a degree somewhere between 0 and MAX_DEGREE.
# It folds the data and uses cross validation.

import numpy as np
import matplotlib.pyplot as plt

MAX_DEGREE = 20
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
    best_func = np.poly1d([0])
    lowest_error = 10000
    average_errors = []

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

        if average_error < lowest_error:
            lowest_error = average_error
            best_func = regression_func

    plt.plot(average_errors)
    plt.show()

def graph_data_and_best_fit(coefficients):
    pass

if __name__ == '__main__':
    coefficients = compute_best_coefficients(all_data)
    graph_data_and_best_fit(coefficients)
    print all_data.shape
