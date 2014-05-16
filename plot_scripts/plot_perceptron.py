#!/usr/bin/env python3

import random, sys
import matplotlib.pyplot as plt

sys.path.append("../")
import perceptron
import synthetic_data

plt.grid()

# initialize prng and weights to get deterministic results
random.seed(2)
w = [2.0, -0.1, -0.8]

# create random examples of two classes
l0, l1 = synthetic_data.binary_class_linsep(100)

x, y = zip(*l0)
plt.plot(x, y, ".", marker = "+")
x, y = zip(*l1)
plt.plot(x, y, ".", marker = "x")
plt.plot(range(6), label = "y = x")

for n in [1, 10, 100, 500, 1000]:
  # plot the decision boundary
  weights, its, err = perceptron.binary_learning(l0, l1,
    maxiterations = n, miniterations = n, weights = w, learning_rate = 0.0001)
  y = [(-weights[0] - weights[1] * x) / weights[2] for x in range(6)]
  plt.plot(y, label = str(n))

weights, its, err = perceptron.binary_learning(l0, l1, weights = w, learning_rate = 0.0001)
print (its, "0.001")
weights, its, err = perceptron.binary_learning(l0, l1, weights = w, learning_rate = 0.1)
print (its, "0.1")

plt.title("learning rate = 0.0001")
plt.legend(loc = "lower right")
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.savefig("perceptron.png")
#plt.show()
