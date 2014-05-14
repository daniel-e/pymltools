import random

def threshold(val):
  if (val > 0.0): return 1.0
  return 0.0

def dotproduct(a, b):
  return sum(i * j for i, j in zip(a, b))

def binary_learning(l0, l1, iterations, learning_rate = 0.1, weights = None, step_function = threshold):
  # x_0 is always on
  # x_1, x_2 = coordinates
  labeled = [(0, i[0], i[1]) for i in l0] + [(1, i[0], i[1]) for i in l1]
  # initialize random weights
  # weights[0] is the bias of the neuron
  if not weights:
    weights = [random.random() for i in range(3)]

  for c in range(iterations):
    for l, x1, x2 in labeled:
      # input x0 is always on because the weight of this input is the bias
      x = [1.0, x1, x2]
      y = step_function(dotproduct(weights, x))
      for i in range(len(weights)):
        weights[i] += (float(l) - y) * learning_rate * x[i]
  return weights
