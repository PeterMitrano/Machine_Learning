#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from random import random

MAX_IT = 100000
LEARNING_RATE = 0.1

all_data = np.array([
    [-33, 14, 0, 0],
    [6, 0,  4, 0],
    [-11, 7, 4, 0],
    [9, 21, 0, 0],
    [11, 15, 0, 0],
    [22, 5, 6, 0],
    [25, -2, 6, 0],
    [27, -6, 6, 0],

    [9, 23, -4, 1],
    [26, 4, 1, 1],
    [37, 10, -4, 1],
    [44, 16, -1, 1],
    [51, 20, -2, 1],
    [55, 9, -5, 1],
    [77, 1, -3, 1],
    ])

if __name__ == '__main__':
    yes_xs = []
    yes_ys = []
    yes_zs = []
    no_zs = []
    no_xs = []
    no_ys = []
    for datum in all_data:
        if (datum[3] == 1):
            yes_xs.append(datum[0])
            yes_ys.append(datum[1])
            yes_zs.append(datum[2])
        else:
            no_xs.append(datum[0])
            no_ys.append(datum[1])
            no_zs.append(datum[2])

    N = len(all_data)
    dim = len(all_data[0])
    w = np.random.random_sample(dim)
    print 'dim:', dim, 'N:', N, 'initial w: ' ,w
    bias = 1
    errors = np.ones(N)
    it = 0

    while it < MAX_IT and not np.array_equal(errors, np.zeros(N)):
        i = 0
        for datum in all_data:
            x = (bias, datum[0], datum[1], datum[2])
            c = datum[3]
            c_hat = 1 if sum(w*x) >= 0 else 0
            error = c - c_hat
            errors[i] = error

            # TESTING
            #r = random()
            #if (r > 0.666):
              #error = 1
            #elif (r < 0.3333):
              #error = -1
            #else:
              #error = 0

            w[0] += LEARNING_RATE * error * bias
            w[1] += LEARNING_RATE * error * datum[0]
            w[2] += LEARNING_RATE * error * datum[1]
            w[3] += LEARNING_RATE * error * datum[2]

            i += 1

        it += 1

        if it % (MAX_IT/1) == 0:
          pass
        print w, errors

    print 'final w: ', w
    print 'final error: ', errors
    print 'iterations needed: ', it

    w[3] = 0.00001 if w[3] == 0 else w[3] # dividing by zero is a no-no

    # any three points define a plane, so pick (0,0), (1,0), (0,1)
    z1 = -(bias * w[0]  + 0 * w[1] + 0 * w[2]) / w[3]
    z2 = -(bias * w[0]  + 1 * w[1] + 0 * w[2]) / w[3]
    z3 = -(bias * w[0]  + 0 * w[1] + 1 * w[2]) / w[3]

    # cross product to get normal vector
    normal = np.array([z3-z1, z2-z1, 1])

    # create x,y for plane
    xx, yy = np.meshgrid(range(10), range(10))

    # calculate corresponding z
    point_on_plane = np.array([0, 0, z1])
    d = -point_on_plane.dot(normal)
    z = (-normal[0] * xx - normal[1] * yy - d) * 1. /normal[2]

    print z1, z2, z3

    figure = plt.figure()
    ax = figure.add_subplot(111, projection="3d")

    ax.set_xlim((min(min(yes_xs, no_xs)), max(max(yes_xs), max(no_xs))))
    ax.set_ylim((min(min(yes_ys, no_ys)), max(max(yes_ys), max(no_ys))))
    ax.set_zlim((min(min(yes_zs, no_zs)), max(max(yes_zs), max(no_zs))))

    ax.scatter(yes_xs, yes_ys, yes_zs, c='r', marker='^')
    ax.scatter(no_xs, no_ys, no_zs, c='b', marker='o')
    ax.plot_surface(xx, yy, z)
    plt.show()

