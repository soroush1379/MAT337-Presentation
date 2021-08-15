import numpy as np
from math import pi, cos
from utils.PlotGrapher import PlotGrapher
from utils.Label import Label
from utils.Trendline import Trendline
from utils.Color import Color
from utils.Legend import Legend
from utils.Legend import Location as LegendLocation

poissonKernal = lambda r, t: 1 / (2 * pi) * (1 - r ** 2) / (1 - 2 * r * cos(t) + r ** 2)
xvals = np.linspace(-pi, pi, 1000)

trendlines = []
radii = [0, 0.6, 0.7, 0.85, 0.9]
lineStyles = ["-", "--", "-.", "-", "--"]
colors = [
    Color(1, 0, 0),
    Color(0, 1, 0),
    Color(0, 0, 1),
    Color(1, 0.5, 0),
    Color(1, 0, 1),
]
for (radius, lineStyle, color) in zip(radii, lineStyles, colors):
    func = lambda t: poissonKernal(radius, t)
    name = "$r = {radius}$".format(radius=radius)
    trendlines.append(
        Trendline.fromLambda(xvals, func)
        .withLineStyle(lineStyle)
        .withColor(color)
        .withName(name)
        .withLineWidth(2)
    )

g = PlotGrapher()

g.setTitle(Label("Poisson's Kernal $P(r, \\theta)$", 50))
g.setXLabel(Label("$\\theta$", 45))
g.setYLabel(Label("$P(r, \\theta)$", 45))

g.setXTickFontSize(15)
g.setYTickFontSize(15)

g.setGrid(True)
g.setFigsize((16, 9))

g.setXLim((-pi, pi))

[g.setTrendline(trendline) for trendline in trendlines]

g.setLegend(
    Legend().withLocation(LegendLocation.BEST).withColumnNumber(1).withFontSize(30)
)

g.show()
# g.save("results/poisson_kernal.png")
