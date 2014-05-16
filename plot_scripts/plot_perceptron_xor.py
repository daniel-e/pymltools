#!/usr/bin/env python3

import random, math, sys
import matplotlib.pyplot as plt

sys.path.append("../")
import perceptron
import synthetic_data

plt.grid()

# initialize prng and weights to get deterministic results
random.seed(2)
w = [2.0, -0.1, -0.8, 0.2]

# create random examples of two classes
l0, l1 = synthetic_data.xor_binary_class(50, 0.5)

# TODO
l0 = list(l0)
l1 = list(l1)

x, y = zip(*l0)
plt.plot(x, y, ".", marker = "+")
x, y = zip(*l1)
plt.plot(x, y, ".", marker = "x")

# map the data into a space with one addition dimension so that
# it becomes linearly separable
l0 = [(x, y, x*y) for x, y in l0]
l1 = [(x, y, x*y) for x, y in l1]

w, its = perceptron.binary_learning(l0, l1, weights = w)
print ("iterations =", its)

def frange(start, end, step):
  r = start
  while r < end:
    yield r
    r += step

# plot the decision boundary
x = list(frange(-2, 0.52, 0.001))
y = []
for i in x:
  a = (-w[0] - w[1] * i) / (w[2] + w[3] * i)
  y.append(a)
plt.plot(x, y, "r", label = "decision boundary")

x = list(frange(0.53, 1.5, 0.001))
y = []
for i in x:
  a = (-w[0] - w[1] * i) / (w[2] + w[3] * i)
  y.append(a)
plt.plot(x, y, "r")


plt.legend(loc = "lower right")
plt.xlim([-0.5, 1.5])
plt.ylim([-0.5, 1.5])
plt.savefig("perceptron_xor.png")
#plt.show()
