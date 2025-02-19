import numpy as np
import matplotlib.pyplot as plt
import spatialmath.base as smb # type: ignore


R = smb.rotx(3.14 / 2)

smb.trplot(R)
smb.tranimate(R)
plt.show()