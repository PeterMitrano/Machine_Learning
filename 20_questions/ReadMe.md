# 20 Questions

If you have a set of hypethesis `H`, and each hypothesis as attributes `A`. Hypethoses are things like "types of cars", or "a set of people", or "any noun". Attributes are yes or no properties like "is it blue", or "does it weight more then 20kg". The users picks one `h` such that `hєH`, and out goal is to guess that `h`. To do, we ask the user up to twenty questions. The best question to ask at each point is the question that provides the most "information", or "decreases entropy" the most. The questions are binary, so a each step the current set of hypothesis will be split into only two groups. If our current set of hypothesis has `n` elements, then after the question one resulting group will be of size `l`, and the other of size `n-l`. So the probability of getting a *yes* is `l/n`, and the probability of getting a *no* is `(n-l)/n`. Therefore, our algorithm for picking the next question is simple: pick the attribute for which `l*l/n + (n-l)*(n-l)/n` is smallest.

## Implementation
We need a dataset. The input needs to have a set of text hypothesis label, and a vector of attributes. Each attribute is a number. We want to track the number of elements `l` for each attribute `a`. We can't treat various levels of continuity or discrete or binary-ness that same. We always want to ask about the value that splits the data the best. If we pick a value of `a` such that `l≃n/2`, then `l*l/n + (n-l)*(n-l)/n = (n/4) + (n/4) = n/2`. So for each attribute, we find the value for that attribute that splits the data in half best, and then out of all those values for all the attributes, we want the value of the attribute that overal splits the data the best. But for discrete values, we can only have one of a set of values, and we need to know that set, and whether an attribute is discrete, binary, or continuous.

Example input:
```
{
  'attributes': [
    {'name': 'edible' 'type': 'boolean'},
    {'name': 'price' 'type': 'continuous'},
    {'name': 'color' 'type': 'discrete'},
  ]
  'data' : [
   {'chair': ['edible': false, 'price': 50, 'color': 'any']},
   {'bed': ['edible': false, 'price': 250, 'color': 'any']},
   {'spoon': ['edible': false, 'price': 0.5, 'color': 'any']},
   {'cheese': ['edible': true, 'price': 10, 'color': ['yellow', 'white', 'orange']},
]}
```
