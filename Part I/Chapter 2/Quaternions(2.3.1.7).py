from spatialmath import SE3, UnitQuaternion # type: ignore
from spatialmath.base import rpy2r # type: ignore
import numpy as np
import matplotlib.pyplot as plt

# Create quaternion from Rotation Matrix
q = UnitQuaternion(rpy2r(0.1,0.2,0.3))

# Get 4x4 Matrix for quaternion
q.matrix

# Quaternion inverse
q.inv()

# Convert to Rotation matrix
q.R

# plotting what this quaternion can do
q.plot()
#plt.show()

# Rotating a coordinate vector using overloaded multiplication
q * [1, 0, 0]



'''
the quaternion functions in the spatialmath.base package consider the
quaternion as a 4-element 1D NumPy array with this ordering. Some software tools,
notably ROS, consider the quaternion as a vector ordered as v x ; v y ; v z ; s
'''