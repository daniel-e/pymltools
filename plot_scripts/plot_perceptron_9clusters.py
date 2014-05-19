#!/usr/bin/env python3

import random, math, sys
import matplotlib.pyplot as plt

sys.path.append("../")
import perceptron, synthetic_data, tools

# initialize prng and weights to get deterministic results
random.seed(2)
w = [2.0, -0.1, -0.8, 0.2, 0.5, 0.2, 0.3, 0.9, 0.7]

# maps a list of two-dimensional points into a list of nine dimensional points
def map_points(p):
  return [(x, y, x+y, x*y, x*x+y*y, x*x*y*y, x*x*x+y*y*y, x*x*x*y*y*y, x*x*x*x*x*y*y*y*y) for x, y in p]

# create random two-dimensional examples in two classes
l0, l1 = [list(i) for i in synthetic_data.alternating_binary_class(3, 3, 0.2, 50)]

# map the data into a space with nine dimension so that
# it becomes linearly separable
lx0, lx1 = [map_points(l0), map_points(l1)]

# train the perceptron with the high dimensional data
w, its, err = perceptron.binary_learning(lx0, lx1, weights = w, maxiterations = 3000, shuffle = True)
print ("iterations =", its, "errors =", err)

# plot the decision boundary
plt.grid()
k = [[], []]
for x, y in tools.xy_tuples(-1, 3, 0.01, -1, 3, 0.01):
  l = map_points([(x, y)])[0]
  k[perceptron.classify(l, w)].append((x, y))
x, y = zip(*k[0])
plt.plot(x, y, ".", color="#ffaaaa", marker=".", markersize=4)
x, y = zip(*k[1])
plt.plot(x, y, ".", color="#ccffcc", marker=".", markersize=4)

# add the examples to the plot
x, y = zip(*l0)
plt.plot(x, y, "r.", marker = "+")
x, y = zip(*l1)
plt.plot(x, y, "g.", marker = "x")

plt.xlim([-0.5, 2.8])
plt.ylim([-0.5, 2.8])
plt.savefig("perceptron_9clusters.png")
plt.show()
