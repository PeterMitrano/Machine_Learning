#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

MAX_IT = 100000
LEARNING_RATE = 0.0005

all_data = np.array([
    [7, 1, 3],
    [4, 4, 4],
    [2, 5, -8],
    [0, 6, 0],
    [-1, 7, -1],
    [5, 9, 3],
    [4, 10, 2],
    [-3, 14, -3],
    [1, 15, -1],
    [4, 16, 8],
    [2, 18, -1],
    [4, 20, 2],
    [1, 21, -5],
    ])


if __name__ == '__main__':
    yes_xs = []
    yes_ys = []
    no_xs = []
    no_ys = []
    for datum in all_data:
        if (datum[2] >= 1):
            yes_xs.append(datum[0])
            yes_ys.append(datum[1])
        else:
            no_xs.append(datum[0])
            no_ys.append(datum[1])

    N = len(all_data)
    w = np.random.random_sample(3)
    print 'initial w: ' ,w
    bias = 1
    errors = np.ones(N)
    it = 0

    while it < MAX_IT and not np.array_equal(errors, np.zeros(N)):
        i = 0
        for datum in all_data:
            x = (bias, datum[0], datum[1])
            y = datum[2]
            y_hat = sum(w*x)
            error = y - y_hat

            w[0] += LEARNING_RATE * error * bias
            w[1] += LEARNING_RATE * error * datum[0]
            w[2] += LEARNING_RATE * error * datum[1]

            errors[i] = error
            i += 1

        it += 1

    print 'final w: ', w
    print 'iterations needed: ', it

    x1 = min(min(no_xs), min(yes_xs))
    x2 =  max(max(no_xs), max(yes_xs))

    w[2] = 0.00001 if w[2] == 0 else w[2] # dividing by zero is a no-no

    y1 = -(bias * w[0]  + x1 * w[1]) / w[2]
    y2 = -(bias * w[0]  + x2 * w[1]) / w[2]

    plt.plot([x1, x2], [y1, y2])
    plt.plot(yes_xs, yes_ys, 'r.')
    plt.plot(no_xs, no_ys, 'b.')
    plt.show()

