from utils.visualization import plot_2D_rational_bezier_curve,\
    plot_2D_parametric_function, plot_3D_bezier_surface, plot_3D_bezier_isocurve
import matplotlib.pyplot as plt
from numpy import asarray, sqrt
from chapter.one import deCasteljau2

points = (
    (asarray([0, 0, 0]), asarray([3, 0, 3]), asarray([6, 0, 3]), asarray([9, 0, 0])),
    (asarray([0, 2, 2]), asarray([3, 2, 5]), asarray([6, 2, 5]), asarray([0, 2, 2])),
    (asarray([0, 4, 0]), asarray([3, 4, 3]), asarray([6, 4, 3]), asarray([9, 4, 0])),
)
fig = plt.figure()
ax = fig.gca(projection='3d')
#
# Plot surface
plot_3D_bezier_surface(points, ax=ax)
#
# Calc point
C = deCasteljau2(points, 2, 3, 1.0/3.0, 1.0/2.0)
ax.scatter([C[0]], [C[1]], [C[2]], color='y', s=100, label="S(1/3, 1/2)")
#
# Plot isocurve
plot_3D_bezier_isocurve(points, 0.5, v_range=(0, 1),
                        num_v_pts=100, ax=ax, label="Isocurve, u = 0.5")

plt.legend()
plt.show()

