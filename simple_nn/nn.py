import matplotlib.pyplot as plt
import numpy as np

def nonlin(x, deriv=False):
    if deriv:
        return x * (1-x)

    else:
        return 1/(1+np.exp(-x))

X = np.array([
        [0,0],
        [0,1],
        [0,0],
        [1,1],
        [1,0],
        [0,1],
        [0,0],
        [1,0],
        [0,1],
        [1,1],
        [1,0],
        [1,1],
        ])

Y = np.array([
    [0],
    [1],
    [0],
    [1],
    [1],
    [1],
    [0],
    [1],
    [1],
    [1],
    [1],
    [1],
    ])

np.random.seed(1)

syn0 = 2 * np.random.random((2,11)) - 1
syn1 = 2 * np.random.random((11,1)) - 1

print "TRAINING"

N = 100
x = []
y = []
for j in xrange(N):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    l2_error = Y - l2

    if (j % 1) == 0:
        S = 20
        err = 0
        for i in xrange(S):
            a = 1 if np.random.uniform() > 0.5 else 0
            b = 1 if np.random.uniform() > 0.5 else 0
            if a or b:
                a_or_b = 1
            else:
                a_or_b = 0
            l0_temp = [[a, b]]
            l1_temp = nonlin(np.dot(l0_temp, syn0))
            l2_temp = nonlin(np.dot(l1_temp, syn1))
            err += abs(a_or_b - l2_temp[0][0])
        x.append(j)
        y.append(err/S)
        print "{0}% \t\t validation error: {1}".format(float(j)/N, err/S)

    l2_delta = l2_error  + nonlin(l2, deriv = True)
    l1_error = l2_delta.dot(syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv = True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

plt.scatter(x, y)
plt.show()
