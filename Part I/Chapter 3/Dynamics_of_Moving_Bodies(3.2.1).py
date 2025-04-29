from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np


J = np.array([[2, -1, 0],
              [-1, 4, 0],
              [0, 0, 3]])

orientation = UnitQuaternion()
w = 0.2*np.array([1, 2, 2])

dt = 0.05

def update():
    global orientation, w
    for t in np.arange(0, 10, dt):
        wd = -np.linalg.inv(J) @ (np.cross(w, J @ w))
        w += wd*dt
        orientation *= UnitQuaternion.EulerVec(w * dt)
        yield orientation.R
        
tranimate(update())
plt.show()