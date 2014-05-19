import random


def threshold(val):
  if (val > 0.0): return 1.0
  return 0.0

def dotproduct(a, b):
  return sum(i * j for i, j in zip(a, b))

def binary_learning(l0, l1, maxiterations = -1, miniterations = -1,
      learning_rate = 0.1,
      weights = None,
      step_function = threshold):
  assert (len(l0) > 0 and len(l1) > 0)
  # x_0 is always on
  # x_1, x_2, ... = coordinates
  labeled = [[0] + list(i) for i in l0] + [[1] + list(i) for i in l1]
  # initialize random weights
  # weights[0] is the bias of the neuron
  dim = len(l0[0])
  w = []
  if not weights:
    w = [random.random() for i in range(dim + 1)]
  else:
    w = list(weights)

  its = 0
  nerrors = 0
  while True:
    if maxiterations != -1 and its >= maxiterations:
      break
    its += 1
    for item in labeled:
      label = item[0]
      # input x0 is always on because the weight of this input is the bias
      x = [1.0] + item[1:]
      y = step_function(dotproduct(w, x))
      d = float(label) - y
      if d != 0:
        for i in range(len(w)):
          w[i] += d * learning_rate * x[i]
    # TODO
    nerrors = 0
    for item in labeled:
      label = item[0]
      x = [1.0] + item[1:]
      y = step_function(dotproduct(w, x))
      d = float(label) - y
      nerrors += abs(d)
    if nerrors == 0:
      if miniterations == -1:
        break
      elif its >= miniterations:
        break
  return w, its, nerrors
