#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

LEARNING_RATE = 0.005

all_data = np.array([
    [1, 7, 1],
    [4, 4, 0],
    [5, 2, 0],
    [6, 0, 0],
    [7, -1, 0],
    [9, 5, 1],
    [10, 4, 1],
    [14, -3, 0],
    [15, 1, 0],
    [16, 4, 1],
    [18, 2, 0],
    [20, 4, 1],
    [21, 1, 0],
    ])


if __name__ == '__main__':
    yes_xs = []
    yes_ys = []
    no_xs = []
    no_ys = []
    for datum in all_data:
        if (datum[2] == 1):
            yes_xs.append(datum[0])
            yes_ys.append(datum[1])
        else:
            no_xs.append(datum[0])
            no_ys.append(datum[1])

    N = len(all_data)
    w = np.random.random_sample(3)
    print w
    bias = 1
    errors = np.ones(N)
    it = 0

    while it < 1000 and not np.array_equal(errors, np.zeros(N)):
        i = 0
        for datum in all_data:
            x = (bias, datum[0], datum[1])
            y = datum[2]
            y_hat = 1 if sum(w*x) >= 0 else 0
            error = y - y_hat

            w[0] += LEARNING_RATE * error * bias
            w[1] += LEARNING_RATE * error * datum[0]
            w[2] += LEARNING_RATE * error * datum[1]

            errors[i] = error
            i += 1

        it += 1

    print w, it

    min_x = min(min(no_xs), min(yes_xs))
    max_x =  max(max(no_xs), max(yes_xs))
    min_y = min(min(no_ys), min(yes_ys))
    max_y =  max(max(no_ys), max(yes_ys))

    line_ys = []
    line_xs = []
    for x in range(min_x, max_x):
        # given x=x, and output=1 solve for y
        w[2] = 0.001 if w[2] == 0 else w[2]
        y = -(bias * w[0]  + x * w[1]) / w[2]

        line_xs.append(x)
        line_ys.append(y)


    plt.plot(line_xs, line_ys)
    plt.plot(yes_xs, yes_ys, 'r.')
    plt.plot(no_xs, no_ys, 'b.')
    plt.show()

