from scipy.optimize import root
from numpy import linspace, zeros, meshgrid
import matplotlib.pyplot as plt

def plot_2D_implicit_function(implicit_function, x_range=(-10, 10,), y_range=(-10, 10), num_pts=100, ax=None,
                              **kwargs):
    #
    # This function assumes that the implicit function
    # is defined in such a way as to be equal to zero.
    # This can be easily accomplished by subtracting
    # any nonzero term from the implicit function
    # definition. 
    x_discretization = linspace(x_range[0], x_range[1], num_pts)
    y_discretization = linspace(y_range[0], x_range[1], num_pts)
    #
    X, Y = meshgrid(x_discretization, y_discretization)
    Z = implicit_function(X, Y)
    #
    # Get contour
    contours = plt.contour(X, Y, Z, [0])
    paths = contours.collections[0].get_paths()[0]
    vertices = paths.vertices
    x = vertices[:, 0]
    y = vertices[:, 1]
    #
    # Either put it on an axis or
    # just use current
    if ax is None:
        ax = plt.gca()
    #
    # Plot
    ax.plot(x, y, **kwargs)
    

def plot_2D_parametric_function(parametric_function, u_range=(0, 1,), num_pts=100, ax=None,
                                **kwargs):
    #
    # discretize
    u_discretization = linspace(u_range[0], u_range[1], num_pts)
    (x, y) = parametric_function(u_discretization)
    #
    # Either put it on an axis or
    # just use current
    if ax is None:
        ax = plt.gca()
    #
    # Plot
    ax.plot(x, y, **kwargs)
