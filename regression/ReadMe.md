# Regression, Overfitting, and Cross-Validation!

This little python demo, which could probably be shortened immensely with other python voodoo, shows my first real machine learning project. I made up some random data points, and wanted to fit a polynomial too them. This script demonstrated overfitting from high order polynomials, and shows how cross-validation can warn us when it is occuring.

The hyperparameters are `MAX_DEGREE` and `k`. Max degree is the highest order polynomial we'll consider. Something around 8 is usually a good demonstration. k is the fraction of data we use for cross-validation. If you have 20 data points, and k=4, then you will always leave out 1/4th (5 points) of the data, and train on 3/4th (15). Then it will calculate average squared error of the trained polynomial on the 1/4th it left out.

here's an example of what you might see if `MAX_DEGREE=12` and `k=4`.
![Image of Yaktocat](https://github.com/petermitrano/Machine_Learning/regression/example.png)
