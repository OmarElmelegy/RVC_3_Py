from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np
from roboticstoolbox import *
from RVC3.examples.imu_data import IMU

true, imu = IMU()

kI = 0.2
kP = 1

b = np.zeros(imu.gyro.shape)
qcf = UnitQuaternion()

data = zip(imu.gyro[:-1], imu.accel[:-1], imu.magno[:-1])

q = UnitQuaternion()
for wm in imu.gyro[:-1]:
    q.append(q[-1] @ UnitQuaternion.EulerVec(wm * imu.dt))

# Create a single figure
plt.figure()

# Plot first line (red) with label
plt.plot(true.t, q.angdist(true.orientation), color="red", label="Gyro only")

# Compute and plot second line (blue) with label
for k, (wm, am, mm) in enumerate(data):
    qi = qcf[-1].inv()
    sR = np.cross(am, qi*true.g) + np.cross(mm, qi * true.B)
    wp = wm - b[k, :] + kP * sR
    qcf.append(qcf[k] @ UnitQuaternion.EulerVec(wp * imu.dt))
    b[k+1, :] = b[k, :] - kI * sR * imu.dt

plt.plot(true.t, qcf.angdist(true.orientation), color="blue", label="Complementary filter")

# Add legend, labels, and display
plt.legend()
plt.xlabel('Time')
plt.ylabel('Angular Distance')
plt.title('Orientation Error Comparison')
plt.grid(True)
plt.show()