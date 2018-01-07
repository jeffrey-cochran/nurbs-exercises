from numpy import asarray
from numpy.linalg import solve
from utils.visualization import plot_2D_power_basis_curve
import matplotlib.pyplot as plt

#
# Construct the matrix of coefficients
# assuming that a_0 is known
Ax = asarray([
    [0.5, 0.25, 0.125],  # C
    [1.0, 1.0, 0.75],    # C'
    [0.0, 2.0, 3.0],     # C''
])
bx = [
    1,  # C
    2,  # C'
    1,  # C''
]
x = solve(Ax, bx)
#
# Repeat for y
Ay = asarray([
    [0.5, 0.25, 0.125],  # C
    [1.0, 1.0, 0.75],    # C'
    [0.0, 2.0, 3.0],     # C''
])
by = [
    1,  # C
    -6,  # C'
    -3,  # C''
]
y = solve(Ay, by)
print(sum(y))
print(sum(x))


points = (
    asarray([1, 1]),
    asarray([0.25, 0.5]),
    asarray([-0.5, -0.5]),
    asarray([1.0/3.0, 0]),
)

plot_2D_power_basis_curve(points, label='Cusp Example')
plt.legend()
plt.show()
