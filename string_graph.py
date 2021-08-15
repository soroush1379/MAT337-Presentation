# MAT337 Assignment - Soroush Khoubyarian
from math import pi, cos, sin, floor, exp, tan
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Change the functions below to see the effects!
initialPosition = lambda x : sin(x**2)
initialSpeed = lambda x : pi/2 - x

# Solving the wave equation
Nmax = 50
v = 1
A = [0]
B = [0]

for n in range(1, Nmax+1):
    A += [quad(lambda x : initialPosition(x) * sin(n*x), 0, pi)[0] / (pi/2)]
    B += [quad(lambda x : initialSpeed(x) * sin(n*x), 0, pi)[0] / (n*pi*v/2)]

wave = lambda x, t : sum([A[n]*sin(n*x)*cos(n*v*t) + B[n]*sin(n*x)*sin(n*v*t) for n in range(Nmax+1)])

# Animating
xvals = np.linspace(0, pi, 50)
tvals = np.linspace(0, 2*pi, 300)
yvals = [[wave(x, t) for x in xvals] for t in tvals]

fig, ax = plt.subplots()
p, = plt.plot([], [], 'r-')
ax.grid()
ax.set_xlabel('x', fontsize=20)
ax.set_ylabel('y', fontsize=20)

def init():
    minY = min(np.array(yvals).flatten())
    maxY = max(np.array(yvals).flatten())
    ax.set_xlim([-0.1, pi+0.1])
    ax.set_ylim([minY - 0.1, maxY + 0.1])
    return p,

def update(frame):
    p.set_data(xvals, yvals[frame])
    return p,

ani = FuncAnimation(fig, update, frames=len(tvals), init_func=init, interval=10, blit=True)
plt.show()
