from roboticstoolbox import *
from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np


R0 = SO3.Rz(-1) * SO3.Ry(1)
R1 = SO3.Rz(1) * SO3.Ry(1)

rpy0 = R0.rpy()
rpy1 = R1.rpy()

tra = mtraj(quintic, rpy0, rpy1, 50)
pose = SO3.RPY(tra.q)

#pose.animate()

q0 = UnitQuaternion(R0)
q1 = UnitQuaternion(R1)

tra_ = q0.interp(q1, 50)
#tra_ = q0.interp(q1, 50, shortest=True)

tra_.animate()

plt.show()


# We cannot linearly interpolate a rotation matrix