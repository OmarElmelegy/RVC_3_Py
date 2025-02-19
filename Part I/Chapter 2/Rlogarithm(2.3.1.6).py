import numpy as np
import matplotlib.pyplot as plt
import spatialmath.base as smb  # type: ignore
from scipy import linalg # type: ignore


R = smb.rotx(0.3)
L = smb.trlog(R)
S = smb.vex(L)

# Skew operator [.]x
X = smb.skew([1, 2, 3])

# Reverse Skew operator Vx(.)
RevX = smb.vex(X)


'''
There are many other situations where we know the orientation in terms of
two vectors. For a camera, we might use the optical axis (by convention the z-
axis) as a and the right-side of the camera (by convention the x-axis) as n.
For a mobile robot, we might use the gravitational acceleration vector measured with
accelerometers (by convention the z-axis) as a, and the heading direction measured
with an electronic compass (by convention the x-axis) as n.
'''
