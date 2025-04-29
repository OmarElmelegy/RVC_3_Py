from roboticstoolbox import *
from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np

via = SO2(30, unit="deg") * np.array([
    [-1, 1, 1, -1, -1], [1, 1, -1, -1, 1]])
tra1 = mstraj(via.T, dt=0.2, tacc=0, qdmax=[2,1])
xplot(tra1.q[:, 0], tra1.q[:, 1], color="red")
tra2 = mstraj(via.T, dt=0.2, tacc=2, qdmax=[2,1])

print(len(tra1), len(tra2))
tra1.plot()
plt.show()