from bdsim import *
from matplotlib import pyplot as plt
#from RVC3.models import lanechange

sim = BDSim()

bd = sim.blockdiagram()

speed = bd.CONSTANT(1, name="speed")
steering = bd.PIECEWISE((0, 0), (3, 0.5), (4, 0), (5, -0.5), (6, 0), name="steering")
vehicle = bd.BICYCLE(name="vehicle")
xyscope = bd.SCOPEXY1(indices=[0, 1], scale=[0, 10, 0, 1.2])
bd.connect(speed, vehicle.v)
bd.connect(steering, vehicle.gamma)
bd.connect(vehicle, xyscope)
bd.compile()

out = sim.run(bd, T=10)

plt.show()