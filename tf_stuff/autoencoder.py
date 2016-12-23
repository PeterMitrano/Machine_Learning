import tensorflow as tf
import numpy as np
import input_data

mnist_width = 28
n_visible = mnist_width * mnist_width
n_hidden = 500
corruption_level = 0.3

X = tf.placeholder("float", [None, n_visible], name='X')

mask = tf.placeholder("float", [None, n_visible], name="mask")

W_init_max = 4 * np.sqrt( 6.0 / (n_visible + n_hidden))
W_init = tf.random_uniform(shape=[n_visible, n_hidden],
        minval=-W_init_max,
        maxval=W_init_max)

W = tf.Variable(W_init, name='W')
b = tf.Variable(tf.zeros([n_hidden]), name="b")

W_prime = tf.transpose(W)
b_prime = tf.Variable(tf.zeros([n_visible]), name="b_prime")

tilde_X = mask * X
Y = tf.nn.sigmoid(tf.matmul(tilde_X, W) + b)
Z = tf.nn.sigmoid(tf.matmul(Y, W_prime) + b_prime)

cost = tf.reduce_sum(tf.pow(X - Z, 2))
train_op = tf.train.GradientDescentOptimizer(0.02).minimize(cost)

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
trX = mnist.train.images
trY = mnist.train.labels
teX = mnist.test.images
teY = mnist.test.labels

tf.scalar_summary("cost", cost)

#print X
#image_features = tf.reshape(Y, [-1, 28, 28, 1])
#tf.image_summary("features", Y, max_images=100)


with tf.Session() as sess:
    writer = tf.train.SummaryWriter("./logs/nn_logs", sess.graph) # for 0.8
    merged = tf.merge_all_summaries()

    tf.initialize_all_variables().run()

    for i in range(10):
        for start,end in zip(range(0, len(trX), 128), range(128, len(trX), 128)):
            input_ = trX[start:end]
            mask_np = np.random.binomial(1, 1 - corruption_level, input_.shape)
            sess.run(train_op, feed_dict={X: input_, mask: mask_np})

        mask_np = np.random.binomial(1, 1 - corruption_level, teX.shape)
        summary, err = sess.run([merged, cost], feed_dict={X: teX, mask: mask_np})
        writer.add_summary(summary, i)
        print i, err
