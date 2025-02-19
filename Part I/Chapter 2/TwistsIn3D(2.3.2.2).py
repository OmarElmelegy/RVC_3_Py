from spatialmath import * # type: ignore
import numpy as np

S = Twist3.UnitRevolute([1, 0, 0], [0, 0, 0])
print(S)