'''
Created on Jan 4, 2018

@author: jeffr
'''
from utils.visualization import plot_2D_implicit_function


def original_implicit_curve(y, x):
    return x**2.0 - 4*x*y + 4*y**2.0 - 4*x - y - 5

plot_2D_implicit_function(original_implicit_curve, num_pts=1000)