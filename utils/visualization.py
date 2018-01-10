from scipy.optimize import root
from numpy import linspace, zeros, meshgrid, allclose, asarray
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from chapter.one import Horner1, deCasteljau1, deCasteljau2

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


def plot_2D_power_basis_curve(points, num_pts=100, ax=None,
                              **kwargs):
    #
    pbc = get_power_basis_curve(points)
    u_disctretization = linspace(0, 1, num_pts)
    x = []
    y = []
    for u in u_disctretization:
        (xi, yi) = pbc(u)
        x.append(xi)
        y.append(yi)
    #
    # Either put it on an axis or
    # just use current
    if ax is None:
        ax = plt.gca()
    #
    # Plot
    ax.plot(x, y, **kwargs)
    #
    return


def plot_2D_bezier_curve(points, u_range=(0, 1,), num_pts=100, include_control_points=True, ax=None,
                         **kwargs):
    #
    u_discretization = linspace(u_range[0], u_range[1], num_pts)
    x = []
    y = []
    for u in u_discretization:
        next_point = deCasteljau1(points, len(points) - 1, u, return_points=False)
        x.append(next_point[0])
        y.append(next_point[1])
    #
    if ax is None:
        ax = plt.gca()
    #
    ax.plot(x, y, **kwargs)
    #
    # Add control points
    if include_control_points:
        xp = []
        yp = []
        for point in points:
            xp.append(point[0])
            yp.append(point[1])
        #
        ax.plot(xp, yp, '-o')
    #
    return


def plot_2D_rational_bezier_curve(points, u_range=(0, 1,), num_pts=100, include_control_points=True, ax=None,
                                  **kwargs):
        #
    u_discretization = linspace(u_range[0], u_range[1], num_pts)
    x = []
    y = []
    for u in u_discretization:
        next_point = deCasteljau1(points, len(points) - 1, u, return_points=False)
        x.append(next_point[0] / next_point[2])
        y.append(next_point[1] / next_point[2])
    #
    if ax is None:
        ax = plt.gca()
    #
    ax.plot(x, y, **kwargs)
    #
    # Add control points
    if include_control_points:
        xp = []
        yp = []
        for point in points:
            xp.append(point[0] / point[2])
            yp.append(point[1] / point[2])
        #
        ax.plot(xp, yp, '-o')
    return


def plot_3D_bezier_surface(points, u_range=(0, 1,), v_range=(0, 1),
                           num_u_pts=20, num_v_pts=20, ax=None,
                           **kwargs):
    #
    u_discretization = linspace(u_range[0], u_range[1], num_u_pts)
    v_discretization = linspace(v_range[0], v_range[1], num_v_pts)
    #
    # Plot a basic wireframe.
    n = len(points) - 1
    m = len(points[0]) - 1
    x = zeros((num_u_pts, num_v_pts))
    y = zeros((num_u_pts, num_v_pts))
    z = zeros((num_u_pts, num_v_pts))
    print(x.shape)
    for i in range(len(u_discretization)):
        for j in range(len(v_discretization)):
            p = deCasteljau2(points, n, m, u_discretization[i], v_discretization[j])
            x[i, j] = p[0]
            y[i, j] = p[1]
            z[i, j] = p[2]
        #
    #
    if ax is None:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
    #
    ax.plot_surface(x, y, z)
    #
    return


def plot_3D_rational_bezier_surface(points, u_range=(0, 1,), v_range=(0, 1),
                                    num_u_pts=20, num_v_pts=20, ax=None,
                                    **kwargs):
    #
    u_discretization = linspace(u_range[0], u_range[1], num_u_pts)
    v_discretization = linspace(v_range[0], v_range[1], num_v_pts)
    #
    # Plot a basic wireframe.
    n = len(points) - 1
    m = len(points[0]) - 1
    x = zeros((num_u_pts, num_v_pts))
    y = zeros((num_u_pts, num_v_pts))
    z = zeros((num_u_pts, num_v_pts))
    print(x.shape)
    for i in range(len(u_discretization)):
        for j in range(len(v_discretization)):
            p = deCasteljau2(points, n, m, u_discretization[i], v_discretization[j])
            x[i, j] = p[0] / p[3]
            y[i, j] = p[1] / p[3]
            z[i, j] = p[2] / p[3]
        #
    #
    if ax is None:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
    #
    ax.plot_surface(x, y, z, **kwargs)
    #
    return


def plot_3D_bezier_isocurve(points, u, v_range=(0, 1),
                         num_v_pts=20, ax=None,
                         **kwargs):
    #
    v_discretization = linspace(v_range[0], v_range[1], num_v_pts)
    #
    # Plot a basic wireframe.
    n = len(points) - 1
    m = len(points[0]) - 1
    #
    # Get control points for bezier curve
    c_list = []
    for i in range(n + 1):
        c_list.append(deCasteljau1(points[i], m, u))
    #
    x = asarray([c[0] for c in c_list])
    y = asarray([c[0] for c in c_list])
    #
    new_points = tuple(asarray(p) for p in c_list)
    x = []
    y = []
    z = []
    for v in v_discretization:
        c = deCasteljau1(new_points, n, v)
        x.append(c[0])
        y.append(c[1])
        z.append(c[2])
    #
    if ax is None:
        fig = plt.figure()
        ax = fig.gca(projection='3d')
    #
    ax.plot(x, y, z, **kwargs)
    #
    return


def visualize_2D_casteljau(points, u, u_range=(0, 1,), num_pts=100, ax=None,
                           **kwargs):
    #
    plot_2D_bezier_curve(points, u_range=u_range, num_pts=num_pts,
                         include_control_points=True, ax=ax, **kwargs)
    C, all_points = deCasteljau1(points, len(points) - 1, u, return_points=True)
    #
    print(C)
    #
    if ax is None:
        ax = plt.gca()
    #
    for current_points in all_points:
        x = []
        y = []
        for point in current_points:
            x.append(point[0])
            y.append(point[1])
        #
        ax.plot(x, y, '-o')
    #
    return


def get_power_basis_curve(points):
    n = len(points) - 1
    #

    def power_basis_curve(u):
        return Horner1(points, n, u)
    #
    return power_basis_curve
