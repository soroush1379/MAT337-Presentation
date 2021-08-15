# MAT337 Assignment - Soroush Khoubyarian

from math import pi, cos
import numpy as np
from utils.PlotGrapher import PlotGrapher
from utils.Label import Label
from utils.Slider import Slider, Orientation
from utils.TrendlineInteractive import TrendlineInteractive
from utils.Color import Color

xvals = np.linspace(-pi, pi, 500)
func = lambda t, r : (1-r**2) / (1 - 2*r*cos(t) + r**2)
sliderR = (
    Slider(0, 0.90, 0.5)
    .withOrientation(Orientation.HORIZONTAL)
    .withLabel(Label("$r$", 20))
    .withColor(Color(1, 0, 1))
    .withThickness(0.05)
    .withLength(0.7)
)
trendlineInteractive = (
        TrendlineInteractive(xvals, func, [sliderR], [])
    .withColor(Color(1, 0, 0))
    .withLineWidth(2)
)

g = PlotGrapher()

g.setGrid(True)

g.setFigsize((12, 7))

g.setTitle(Label("Poisson's Kernal $P(r, \\theta)$", 40))
g.setXLabel(Label("$\\theta$", 30))
g.setYLabel(Label("$P(r, \\theta)$", 30))

g.setXTickFontSize(20)
g.setYTickFontSize(20)

g.setTrendlineInteractive(trendlineInteractive)

g.setXLim((-pi, pi))
g.setYLim((0, 10))

g.setSliderHorizontalPadding(0.2)
g.setSliderHorizontalBottom(0.05)
g.setSliderHorizontalLeft(0.1)
g.setSliderVerticalBottom(0)
g.setSliderVerticalPadding(0)
g.setSliderVerticalLeft(0.1)

g.show()
