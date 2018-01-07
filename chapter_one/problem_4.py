'''
Created on Jan 4, 2018

@author: jeffr
'''
import matplotlib.pyplot as plt
from utils.visualization import plot_2D_implicit_function,\
    plot_2D_parametric_function


#
# Define the original implicit equation
def original_implicit_curve(x, y):
    return x**2.0 - 4*x*y + 4*y**2.0 - 4*x - y - 5


#
# Define rotated 90deg + translated (-1, -1) implicit equation
def transformed_implicit_curve(x, y):
    return y**2.0 + 4*x**2.0 + 4*x*y + 2*y + 13*x - 3


#
# Define original parametric curve
def original_parametric_curve(u):
    return (-1 - u + (2 * u**2.0), (-2 * u) + u**2.0)


#
# Define the transformed parametric curve
def transformed_parametric_curve(u):
    return (-1 + (2 * u) - u**2.0, -2 - u + (2 * u**2.0))


#
# Plot the original implicit equation
plot_2D_implicit_function(original_implicit_curve, label='Original Implicit Equation')


#
# Plot the transformed implicit equation
plot_2D_implicit_function(transformed_implicit_curve, label='Transformed Implicit Equation')

plt.legend()
plt.show()
plt.clf()


#
# Plot the original parametric equation
plot_2D_parametric_function(original_parametric_curve, u_range=(-5, 5), label='Original Parametric Equation')


#
# Plot the original parametric equation
plot_2D_parametric_function(transformed_parametric_curve, u_range=(-5, 5), label='Transformed Parametric Equation')


plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.legend()
plt.show()
