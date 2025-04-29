from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np
from roboticstoolbox import *
from RVC3.examples.imu_data import IMU


true, imu = IMU()

q = UnitQuaternion()
for wm in imu.gyro[:-1]:
    q.append(q[-1] @ UnitQuaternion.EulerVec(wm * imu.dt))
    
xplot(true.t, q.angdist(true.orientation), color="red")

plt.show()