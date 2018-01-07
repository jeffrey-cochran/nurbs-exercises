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
print(x)
print(y)
#
# Fix a0
a0 = asarray([0, 0])
#
# Construct a1, a2, a3
a1 = asarray([x[0], y[0]])
a2 = asarray([x[1], y[1]])
a3 = asarray([x[2], y[2]])
points = (
    a0,
    a1,
    a2,
    a3,
)

plot_2D_power_basis_curve(points, label='Inflection Point Example')
plt.legend()
plt.show()
