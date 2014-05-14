import random

def random_data(n):
  for i in range(n):
    yield random.random()

def binary_class_linsep(n):
  l0 = [(i * 5.0, random.random() * i * 5.0 * 0.95) for i in random_data(n)]
  l1 = [(i * 5.0, 5.0 - random.random() * (5.0 - i * 5.0) * 0.95) for i in random_data(n)]
  return (l0, l1)
