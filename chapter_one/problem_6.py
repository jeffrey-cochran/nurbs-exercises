from numpy import asarray
from utils.visualization import plot_2D_power_basis_curve
import matplotlib.pyplot as plt


points = (
    asarray([-1, -1]),
    asarray([1, 1]),
    asarray([-1.5, -1.5]),
    asarray([2, -2]),
)

plot_2D_power_basis_curve(points)
plt.show()
