from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np


R1 = rotx(0.3) # create SO(3) matrix as NumPy array
#print(type(R1))

R2 = SO3.Rx(0.3) # Create SO3 object
#print(type(R2))

R2_numpyArray = R2.A # Extracts array from object

# some conversions
R2.rpy()
R2.eul()

# you can do something like this
TA1 = transl2(1, 2) @ trot2(30, "deg")
TA2 = SE2(1, 2) * SE2(30, unit="deg")
TA3 = SE2(1, 2, 30, unit="deg")

#print(TA1)
print(TA2)
#print(TA3)

R2.plot(frame="A")
TA3.plot(frame="B")

#plt.show()

# you can also do this
TA4 = TA2 + TA3
print(TA4)

# These classes inherit from the python list class
R_list = SO3.Rx(np.linspace(0, 1, 5))
#print(R_list)

# It also supports broadcasting
V_Rotated = R_list*[1, 2, 3]
#print(V_Rotated)