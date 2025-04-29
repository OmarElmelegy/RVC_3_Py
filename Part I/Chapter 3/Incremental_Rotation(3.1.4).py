from spatialmath import *
from spatialmath.base import *
import matplotlib.pyplot as plt
import numpy as np
import time

Rexact = np.eye(3) # null rotation
Rapprox = np.eye(3) # null rotation

w = np.array([1,0,0]) # rotation of 1rad/s about x-axis

dt = 0.01
t0 = time.process_time()

for i in range(100):
    Rexact = Rexact @ trexp(skew(w*dt)) #update by composition

print("Time for composition: " + str(time.process_time() - t0) + " seconds")

t0  = time.process_time()

for i in range(100):
    Rapprox += Rapprox @ skew(w*dt) #update by addition

print("Time for addition: " + str(time.process_time() - t0) + " seconds")

print(np.linalg.det(Rapprox) - 1)
print(np.linalg.det(Rexact) - 1)

print(tr2angvec(trnorm(Rexact)))
print(tr2angvec(trnorm(Rapprox)))

'''
In this section we have updated rotation matrices by addition, but addition is not
a group operation for SO(3) The resulting matrix will not belong to SO(3) its
determinant will not equal one and its columns will not be orthogonal unit vectors.
Similarly, we have updated unit quaternions by addition which is not a group operation for S^3 .
The result will not be a proper unit quaternion belonging to S^3 its magnitude will not be one.
However, if the values we add are small, then this problem is minor, and can be
largely corrected by normalization as discussed in 7 Sect. 2.4.6. We can ensure that
those values are small by ensuring that t is small which implies a high sample rate.
For inertial navigation systems operating on low-end computing hardware, there is a
tradeoff between sample rate and accuracy when using approximate update methods.
'''