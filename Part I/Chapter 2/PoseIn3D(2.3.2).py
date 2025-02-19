from spatialmath import SE3 # type: ignore
from spatialmath.base import transl, trotx ,trplot, t2r, vexa, skewa, trlog, trexp # type: ignore
import matplotlib.pyplot as plt
from scipy import linalg # type: ignore
import numpy as np

T = transl(2, 0, 0) @ trotx(np.pi / 2) @ transl(0, 1, 0)
trplot(T)

# Extract components
R = t2r(T)
t = transl(T)

# Some operations
T = transl(2, 3, 4) @ trotx(0.3)
L = trlog(T)
S = vexa(L)
T_reconstructed = trexp(skewa(S))
print(T)
print()
print(T_reconstructed)

plt.show()