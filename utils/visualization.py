from scipy.optimize import root
from numpy import linspace, zeros
import matplotlib.pyplot as plt

def plot_2D_implicit_function(implicit_function, x_range=(0, 10,), num_pts=100):
    #
    x_discretization = linspace(x_range[0], x_range[1], num_pts)
    #
    y = zeros(x_discretization.shape)
    for i in range(x_discretization.shape[0]):
        res = root(implicit_function, x0=[0], args=(x_discretization[i],))
        y[i] = res.x
    print(sum(implicit_function(y, x_discretization)))
    #
    plt.plot(x_discretization, y)
    plt.show()
    

def implicit_parabola(y, x):
    return x**2.0 - y
