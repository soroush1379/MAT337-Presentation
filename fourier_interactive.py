# MAT337 Assignment - Soroush Khoubyarian
from math import pi, cos, sin, floor
import numpy as np
from scipy.integrate import quad
from utils.PlotGrapher import PlotGrapher
from utils.Legend import Legend, Location
from utils.Label import Label
from utils.Slider import Slider, Orientation
from utils.Trendline import Trendline
from utils.TrendlineInteractive import TrendlineInteractive
from utils.Color import Color

# Available functions to test; feel free to add more functions below
absoluteFunction = lambda x : 5*abs(x)
linearFunction = lambda x : x
parabolaFunction = lambda x : (x ** 2) / 5
powerFunction = lambda x : (x ** 8) / 5
arbitraryFunction = lambda x : 10 * (x ** 2)  - x**4 + 2*cos(x)
discontinuousFunction = lambda x : 1 if x > 0 else -1

# Change the line below to switch functions
function = discontinuousFunction

# Fourier coeffieicnts
Nmax = 50
A = [quad(function, -pi, pi)[0] / (2 * pi)]
B = [0]

for n in range(1, Nmax):
    A += [quad(lambda x: function(x) * cos(n * x), -pi, pi)[0] / pi]
    B += [quad(lambda x: function(x) * sin(n * x), -pi, pi)[0] / pi]

# Defining the fourier function
fourierFunction = lambda x, N: sum(
    [A[n] * cos(n * x) for n in range(floor(N) + 1)]
    + [B[n] * sin(n * x) for n in range(floor(N) + 1)]
)

# Creating the trendlines
xvals = np.linspace(-pi, pi, 1000)
functionYvals = [function(x) for x in xvals]

slider = Slider(1, Nmax, 5).withLabel(Label('N', 20)).withValueFormat('%d').withLength(0.7)

functionTrendline = (
    Trendline(xvals, functionYvals)
    .withName("Raw Function")
    .withLineWidth(2)
    .withLineStyle("-")
    .withColor(Color(1, 0, 0))
)
fourierTrendline = (
    TrendlineInteractive(xvals, fourierFunction, [slider], [])
    .withName("Fourier Function")
    .withLineWidth(2)
    .withLineStyle("--")
    .withColor(Color(0, 0, 1))
)

# Plotting
g = PlotGrapher()

g.setGrid(True)

g.setFigsize((12, 7))

g.setTitle(Label("Fourier Transform", 40))
g.setXLabel(Label("$\\theta$", 30))
g.setYLabel(Label("$y(\\theta)$", 30))

g.setXTickFontSize(20)
g.setYTickFontSize(20)

g.setXLim((-pi, pi))

g.setTrendline(functionTrendline)
g.setTrendlineInteractive(fourierTrendline)
g.setLegend(Legend().withLocation(Location.BEST).withFontSize(20))

g.setSliderHorizontalPadding(0.2)
g.setSliderHorizontalBottom(0.05)
g.setSliderHorizontalLeft(0.1)
g.setSliderVerticalBottom(0)
g.setSliderVerticalPadding(0)
g.setSliderVerticalLeft(0.1)

g.show()
