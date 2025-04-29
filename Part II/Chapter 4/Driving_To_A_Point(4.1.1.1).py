import bdsim 
import math
from matplotlib import pyplot as plt
#from RVC3.models import drivepoint

pgoal = [5, 5]
qs = (5, 2, 0)

sim = bdsim.BDSim(animation=True)

bd = sim.blockdiagram()


def background_graphics(ax):
    ax.plot(pgoal[0], pgoal[1], "*")
    ax.plot(qs[0], qs[1], "o")


goal = bd.CONSTANT(pgoal, name="goal")
pos_error = bd.SUM("+-")
d2goal = bd.FUNCTION(lambda d: math.sqrt(d[0] ** 2 + d[1] ** 2))
h2goal = bd.FUNCTION(lambda d: math.atan2(d[1], d[0]))
heading_error = bd.SUM("+-", mode="c")
Kv = bd.GAIN(0.5)
Kh = bd.GAIN(1.5)
bike = bd.BICYCLE(x0=qs, name="vehicle")
vplot = bd.VEHICLEPLOT(
    scale=[0, 10], size=0.7, shape="box", path="b:", init=background_graphics
)  # , movie='rvc4_4.mp4')
vscope = bd.SCOPE(name="velocity")
hscope = bd.SCOPE(name="heading")


xy = bd.INDEX([0, 1], name="xy")
theta = bd.INDEX([2], name="theta")

bd.connect(goal, pos_error[0])
bd.connect(pos_error, d2goal, h2goal)
bd.connect(d2goal, Kv)
bd.connect(Kv, bike.v, vscope)
bd.connect(h2goal, heading_error[0])
bd.connect(theta, heading_error[1])
bd.connect(heading_error, Kh, hscope)
bd.connect(Kh, bike.gamma)
bd.connect(bike, xy, theta, vplot)
bd.connect(xy, pos_error[1])

bd.compile()


sim.report(bd)
out = sim.run(bd, T=10)