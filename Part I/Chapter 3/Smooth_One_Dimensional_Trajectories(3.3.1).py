from roboticstoolbox import *
from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np


tra = quintic(0, 1, np.linspace(0, 1, 50), qd0=10, qdf=0)
#tra.plot()

trap = trapezoidal(0, 1, np.linspace(0, 1, 50), V=1.9)
print(trap.qd.max())
trap.plot()


plt.show()