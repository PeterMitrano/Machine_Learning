#!/usr/bin/python2

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import  matplotlib.image as mping

filename = './MarshOrchid.jpg'
image = mping.imread(filename)
w, h, d = image.shape
x = tf.Variable(image)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("/tmp/basic", sess.graph)
    sess.run(init)
    y = tf.reverse_sequence(x, np.ndarray([w]) * h, 1, batch_dim=0)
    print tf.shape(x).eval(), tf.size(x).eval()
    result = sess.run(y)
    plt.imshow(result)
    plt.show()
