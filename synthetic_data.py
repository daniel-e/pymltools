#!/usr/bin/env python3

import random
from itertools import chain

def random_data(n):
  for i in range(n):
    yield random.random()

def binary_class_linsep(n):
  l0 = [(i * 5.0, random.random() * i * 5.0 * 0.95) for i in random_data(n)]
  l1 = [(i * 5.0, 5.0 - random.random() * (5.0 - i * 5.0) * 0.95) for i in random_data(n)]
  return (l0, l1)

def select(dr, tr, n):
  r = []
  while len(r) < n:
    x = (0.5 - random.random()) * 2.0 * (dr + tr)
    y = (0.5 - random.random()) * 2.0 * (dr + tr)
    rr = x*x + y*y
    if abs(rr - dr) < tr:
      r.append((x, y))
  return r

def binary_class_non_linsep(n):
  l0 = select(1.0, 0.1, n)
  l1 = select(2.0, 0.2, n)
  return (l0, l1)

def cloud(x, y, delta, n):
  for i in range(n):
    a = random.random() * delta - delta / 2.0
    b = random.random() * delta - delta / 2.0
    yield (x + a, y + b)

def xor_binary_class(n, width = 0.2):
  l0 = chain(cloud(0, 0, width, n), cloud(1, 1, width, n))
  l1 = chain(cloud(0, 1, width, n), cloud(1, 0, width, n))
  return [l0, l1]

def alternating_binary_class(columns, rows, width, n):
  l0 = []
  l1 = []
  for i in range(rows):
    for j in range(columns):
      k = i * columns + j
      l = list(cloud(j, i, width, n))
      if k % 2 == 0:
        l0 = l0 + l
      else:
        l1 = l1 + l
  return [l0, l1]
