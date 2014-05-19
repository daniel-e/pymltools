#!/usr/bin/env python3

import random, math, sys
import matplotlib.pyplot as plt

sys.path.append("../")
import perceptron
import synthetic_data

plt.grid()

# initialize prng and weights to get deterministic results
random.seed(2)
w = [2.0, -0.1, -0.8, 0.2, 0.5, 0.2, 0.3, 0.9, 0.7]

# create random examples of two classes
l0, l1 = synthetic_data.alternating_binary_class(3, 3, 0.2, 50)

# TODO
l0 = list(l0)
l1 = list(l1)

def map_points(p):
  return [(x, y, x+y, x*y, x*x+y*y, x*x*y*y, x*x*x+y*y*y, x*x*x*y*y*y, x*x*x*x*x*y*y*y*y) for x, y in p]

# map the data into a space with one addition dimension so that
# it becomes linearly separable
lx0 = map_points(l0)
lx1 = map_points(l1)

w, its, err = perceptron.binary_learning(lx0, lx1, weights = w, maxiterations = 3000)
print ("iterations =", its, "errors =", err)

def frange(start, end, step):
  r = start
  while r < end:
    yield r
    r += step

k0 = []
k1 = []
for x in frange(-1, 3, 0.01):
  for y in frange(-1, 3, 0.01):
    j, a, b, c, d, e, f, g, h = w
    l = map_points([(x, y)])[0]
    r = perceptron.threshold(perceptron.dotproduct(w, [1.0] + list(l)))
    if r > 0:
      k1.append((x, y))
    else:
      k0.append((x, y))
x, y = zip(*k0)
plt.plot(x, y, ".", color="#ffaaaa", marker=".", markersize=4)
x, y = zip(*k1)
plt.plot(x, y, ".", color="#ccffcc", marker=".", markersize=4)


x, y = zip(*l0)
plt.plot(x, y, "r.", marker = "+")
x, y = zip(*l1)
plt.plot(x, y, "g.", marker = "x")

plt.xlim([-0.5, 2.8])
plt.ylim([-0.5, 2.8])
plt.savefig("perceptron_9clusters.png")
#plt.show()
