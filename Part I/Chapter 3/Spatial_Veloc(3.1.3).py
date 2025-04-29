from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np

aTb = SE3.Tx(-2) * SE3.Rz(-np.pi/2) * SE3.Rx(np.pi/2)

bV = np.linspace(1,6,num=6)

aJb = aTb.jacob() # Jacobian

aV = aJb @ bV

print(bV)
print(aV)

