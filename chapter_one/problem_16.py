import matplotlib.pyplot as plt
from utils.visualization import plot_2D_parametric_function


def parametric_circle(u):
    return ((1-u**2.0)/(1+u**2.0), (2 * u) / (1 + u**2.0))


plot_2D_parametric_function(parametric_circle, u_range=(0, 1), color="#ffbdbd", linewidth=4, label="u in (0,1)")
plot_2D_parametric_function(parametric_circle, u_range=(1, 10000), num_pts=100000, color="#f1cbff", linewidth=4, label="u in [1, Infinity)")
plot_2D_parametric_function(parametric_circle, u_range=(-1, 0), num_pts=1000, color="#c9c9ff", linewidth=4, label="u in (-1,0]")
plot_2D_parametric_function(parametric_circle, u_range=(-10000, -1), num_pts=100000, color="#e1f7d5", linewidth=4, label="u in (-Infinity, -1]")

plt.legend()
plt.show()
