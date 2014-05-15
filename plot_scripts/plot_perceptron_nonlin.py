#!/usr/bin/env python3

import random, math, sys
import matplotlib.pyplot as plt

sys.path.append("../")
import perceptron
import synthetic_data

plt.grid()

# initialize prng and weights to get deterministic results
random.seed(2)
w = [2.0, -0.1, -0.8, 0.3]

# create random examples of two classes
l0, l1 = synthetic_data.binary_class_non_linsep(300)

x, y = zip(*l0)
plt.plot(x, y, ".", marker = "+")
x, y = zip(*l1)
plt.plot(x, y, ".", marker = "x")

# map the data into a space with one addition dimension so that
# it becomes linearly separable
l0 = [(x, y, x*x + y*y) for x, y in l0]
l1 = [(x, y, x*x + y*y) for x, y in l1]

w, its = perceptron.binary_learning(l0, l1, maxiterations = 1000, weights = w)
print ("iterations =", its)

def frange(start, end, step):
  r = start
  while r < end:
    yield r
    r += step

# plot the decision boundary
xc = list(frange(-1.2635, 1.1220, 0.0001))
y1 = []
y2 = []
for x in xc:
  c = (w[0] + w[1] * x + w[3] * x * x) / (-w[3])
  p = w[2] / w[3] / 2.0
  y1.append(math.sqrt(c + math.pow(p, 2)) - p)
  y2.append(-math.sqrt(c + math.pow(p, 2)) - p)
plt.plot(xc, y1, "r", label = "decision boundary")
plt.plot(xc, y2, "r")

plt.legend(loc = "lower right")
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.savefig("perceptron_nonlin.png")
plt.show()
