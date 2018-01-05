from numpy import asarray
from utils.visualization import plot_2D_power_basis_curve
import matplotlib.pyplot as plt


points = (
    asarray([0.25, 0.625]),
    asarray([5.5, 2]),
    asarray([-12, -2]),
    asarray([8, 0]),
)

plot_2D_power_basis_curve(points)
plt.show()
