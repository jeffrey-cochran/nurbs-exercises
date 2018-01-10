import matplotlib.pyplot as plt
from numpy import asarray
from utils.visualization import plot_3D_rational_bezier_surface


fig = plt.figure()
ax = fig.gca(projection='3d')


original_points_1 = (
    asarray([1, 1, 0, 1]),
    asarray([1, 1, 1, 1]),
    asarray([2, 0, 2, 2]),
)

original_points_2 = (
    asarray([-1, 1, 0, 1]),
    asarray([-1, 1, 1, 1]),
    asarray([-2, 0, 2, 2]),
)

original_points = (
    original_points_1,
    original_points_2
)

plot_3D_rational_bezier_surface(original_points, ax=ax, color='c', alpha=0.5)

modified_points_1 = (
    asarray([1, 0, 0, 1]),
    asarray([1, 0, 0, 1]),
    asarray([1, 0, 0, 2]),
)

modified_points_2 = (
    asarray([-1, 1, 0, 1]),
    asarray([-1, 1, 1, 1]),
    asarray([-2, 0, 2, 2]),
)

modified_points = (
    modified_points_1,
    modified_points_2
)

plot_3D_rational_bezier_surface(modified_points, ax=ax, color='y', alpha=0.5)

plt.show()
