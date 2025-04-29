from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np
from roboticstoolbox import *
from RVC3.examples.imu_data import IMU


true, _ = IMU()
orientation = UnitQuaternion()

for w in true.omega[:-1]:
    next = orientation[-1] @ UnitQuaternion.EulerVec(w * true.dt)
    orientation.append(next)

orientation.animate(time=true.t)
xplot(true.t, orientation.rpy(), labels="roll pitch yaw")

plt.show()