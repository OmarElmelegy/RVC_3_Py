from roboticstoolbox import *
from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np


tra = mtraj(trapezoidal, [0, 2], [1, -1], 50)

'''
T = SE3()
q = np.array([T.t, T.rpy()])
qf = np.array([[1, 2, 3], [0.9, 0.5, 0.3]])

tra = mtraj(trapezoidal, q0=q, qf=qf, t=50)
'''

tra.plot()
plt.show()
