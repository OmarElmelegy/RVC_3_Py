from roboticstoolbox import *
from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np

T0 = SE3.Trans([0.4, 0.2, 0]) * SE3.RPY(0, 0, 3)
T1 = SE3.Trans([-0.4, -0.2, 0.3]) * SE3.RPY(-np.pi/4, np.pi/4, -np.pi/2)

Ts = T0.interp(T1,50)

Ts.animate()
P = Ts.t
#xplot(P, labels="x y z")

rpy = Ts.rpy()
#xplot(rpy, labels="roll pitch yaw")

Ts = ctraj(T0, T1, 50)
#xplot(Ts.rpy(), labels="roll pitch yaw")

plt.show()