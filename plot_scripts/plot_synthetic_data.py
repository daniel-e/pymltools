#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
sys.path.append("../")
import synthetic_data

def show_plot_classes(data):
  markers = "+xo<D"
  plt.grid()
  for i, l in enumerate(data):
    x, y = zip(*l)
    plt.plot(x, y, ".", marker = markers[i % len(markers)])
  return plt

if __name__ == "__main__":
  plt.figure()
  l0, l1 = synthetic_data.binary_class_linsep(100)
  plt = show_plot_classes([l0, l1])
  plt.plot(range(6))
  plt.title("linearly separable data set")
  plt.xlim([0, 5])
  plt.ylim([0, 5])
  plt.savefig("syn_1.png")
  #plt.show()

  plt.figure()
  l0, l1 = synthetic_data.binary_class_non_linsep(300)
  plt = show_plot_classes([l0, l1])
  plt.title("non-linearly separable data set")
  plt.xlim([-2, 2])
  plt.ylim([-2, 2])
  plt.savefig("syn_2.png")
  #plt.show()

  plt.figure()
  l0, l1 = synthetic_data.xor_binary_class(50, 0.5)
  plt = show_plot_classes([l0, l1])
  plt.title("xor data set")
  plt.xlim([-0.5, 1.5])
  plt.ylim([-0.5, 1.5])
  plt.savefig("syn_3.png")
  #plt.show()
