import matplotlib.pyplot as plt
import synthetic_data

def show_plot_classes(data):
  markers = "+xo<D"
  plt.grid()
  for i, l in enumerate(data):
    x = [j[0] for j in l]
    y = [j[1] for j in l]
    plt.plot(x, y, ".", marker = markers[i % len(markers)])
  plt.plot(range(6))
  plt.title("linearly separable data")
  plt.xlim([0, 5])
  plt.ylim([0, 5])
  plt.show()

if __name__ == "__main__":
  l0, l1 = synthetic_data.binary_class_linsep(100)
  show_plot_classes([l0, l1])
