import matplotlib.pyplot as plt
import synthetic_data

def show_plot_classes(data):
  markers = "+xo<D"
  plt.grid()
  for i, l in enumerate(data):
    x = [j[0] for j in l]
    y = [j[1] for j in l]
    plt.plot(x, y, ".", marker = markers[i % len(markers)])
  plt.xlim([0, 5])
  plt.ylim([0, 5])
  return plt

if __name__ == "__main__":
  l0, l1 = synthetic_data.binary_class_linsep(100)
  plt = show_plot_classes([l0, l1])
  plt.plot(range(6))
  plt.title("linearly separable data")
  plt.show()

  l0, l1 = synthetic_data.binary_class_non_linsep(300)
  plt = show_plot_classes([l0, l1])
  plt.title("non-linearly separable data")
  plt.xlim([-2, 2])
  plt.ylim([-2, 2])
  plt.show()
