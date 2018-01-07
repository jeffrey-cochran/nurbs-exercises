from numpy import asarray
from utils.visualization import plot_2D_power_basis_curve
import matplotlib.pyplot as plt


points = (
    asarray([0.25, 0.625]),
    asarray([5.5, 2]),
    asarray([-12, -2]),
    asarray([8, 0]),
)

plot_2D_power_basis_curve(points, label='Loop Example')
plt.xlim(0.5, 1.5)
plt.ylim(0.5, 1.5)
plt.legend()
plt.show()
