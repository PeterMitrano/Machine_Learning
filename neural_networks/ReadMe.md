# Finding a half plane in linearly seperable data!

This little python demo, which could probably be shortened immensely with other python voodoo, shows my second real machine learning project. I made up some random data points, and wanted to find a line that split the yes and no points. This script demonstrats using a classical thresholded perceptron model to find the weights for the inputs (bias, x, y) that map it to a yes or a no.

The one hyperparameter is the learning rate `LEARNING_RATE`.

here's an example of what you might see if `LEARNING_RATE=0.05`.

![Example output of trained neural net](https://raw.githubusercontent.com/PeterMitrano/Machine_Learning/master/neural_networks/perceptron_rule.png)

just run `./perceptron_rule.py`

## Dependencies

 - matplotlib
 - numpy
