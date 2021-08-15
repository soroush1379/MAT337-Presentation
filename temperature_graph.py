# MAT337 Assignment - Soroush Khoubyarian
from math import pi, cos, sin, floor, exp
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

Nmax = 50

# Boundary Function - Feel free to add your own functions below
parabolaFunction = lambda t : t**2
arbitraryFunction = lambda t : t**2 - 4*t**4 + 5*t**6
arbitraryFunction2 = lambda t : exp(abs(t)) - t**2 - (t**4)/5
constantFunction = lambda t : 1

function = parabolaFunction

# Fourier Function and Solution
A = [quad(function, -pi, pi)[0] / (2*pi)]
B = [0]
for n in range(1, Nmax+1):
    A += [quad(lambda x : function(x) * cos(n*x), -pi, pi)[0] / pi]
    B += [quad(lambda x : function(x) * sin(n*x), -pi, pi)[0] / pi]

fourierFunction = lambda r, t : sum([A[n]*(r**n)*cos(n*t)+B[n]*(r**n)*sin(n*t) for n in range(Nmax+1)])

# Plotting the temperature function
rvals = np.linspace(0,1,50)
thetavals = np.linspace(-pi,pi,50)
R, Theta = np.meshgrid(rvals, thetavals)

X = R * np.cos(Theta)
Y = R * np.sin(Theta)
Z = np.array([[fourierFunction(r, theta) for r in rvals] for theta in thetavals])

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

# Plotting the boundary condition
tvals = np.linspace(-pi, pi, 100)
x = [cos(t) for t in tvals]
y = [sin(t) for t in tvals]
z = [function(t) for t in tvals]
ax.plot3D(x, y, z, 'red', linewidth=3)

ax.set_xlabel('X', fontsize=20)
ax.set_ylabel('Y', fontsize=20)
ax.set_zlabel('Z', fontsize=20)

plt.show()
