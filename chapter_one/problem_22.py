from chapter.one import deCasteljau1
from numpy import asarray

points_1 = (
    asarray([1, 1, 0, 1]),
    asarray([1, 1, 1, 1]),
    asarray([2, 0, 2, 2]),
)

points_2 = (
    asarray([-1, 1, 0, 1]),
    asarray([-1, 1, 1, 1]),
    asarray([-2, 0, 2, 2]),
)

print("Q0 = ", deCasteljau1(points_1, 2, 1.0/3.0))
print("Q1 = ", deCasteljau1(points_2, 2, 1.0/3.0))
