from utils.visualization import plot_2D_bezier_curve, visualize_2D_casteljau
import matplotlib.pyplot as plt
from numpy import asarray

points = (
    asarray([0, 6]),
    asarray([3, 6]),
    asarray([6, 3]),
    asarray([6, 0]),
)

visualize_2D_casteljau(points, 1.0/3.0)

plt.show()
