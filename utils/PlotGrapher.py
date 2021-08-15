import tkinter
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.widgets import Slider as PlotSlider
from utils.Label import Label
from utils.Trendline import Trendline
from utils.TrendlineInteractive import TrendlineInteractive
from utils.Slider import Slider, Orientation
from utils.Color import Color
from utils.Legend import Legend


class PlotGrapher:
    # Inputs
    title = Label
    xlabel = Label
    ylabel = Label
    grid = bool
    legend = Legend
    figsize = int
    xTickFontSize = int
    yTickFontSize = int
    xlim = tuple
    ylim = tuple
    trendlines = list
    trendlineInteractives = list
    sliderHorizontalPadding = float
    sliderVerticalPadding = float
    sliderHorizontalBottom = float
    sliderVerticalLeft = float
    sliderHorizontalLeft = float
    sliderVerticalBottom = float

    # Variables

    trendlineInteractivePlots = list
    trendlineInteractivePlotSliders = list
    fig = None  # matplotlib fig

    def __init__(self):
        # Inputs
        self.title = None
        self.xlabel = None
        self.ylabel = None
        self.grid = False
        self.legend = None
        self.figsize = None
        self.xTickFontSize = None
        self.yTickFontSize = None
        self.xlim = None
        self.ylim = None
        self.trendlines = []
        self.trendlineInteractives = []
        self.sliderHorizontalPadding = None
        self.sliderVerticalPadding = None
        self.sliderHorizontalBottom = None
        self.sliderVerticalLeft = None
        self.sliderHorizontalLeft = None
        self.sliderVerticalBottom = None

        # Variables
        self.trendlineInteractivePlots = []
        self.trendlineInteractivePlotSliders = []
        self.fig = None
        self.ax = None

        self.__setupMatplotlib()

    # SETTERS AND MODIFIERS

    def __setupMatplotlib(self) -> None:
        matplotlib.use("tkagg")
        matplotlib.rcParams["mathtext.fontset"] = "stix"
        matplotlib.rcParams["font.family"] = "STIXGeneral"

    def setTitle(self, title: Label) -> None:
        self.title = title

    def setXLabel(self, xlabel: Label) -> None:
        self.xlabel = xlabel

    def setYLabel(self, ylabel: Label) -> None:
        self.ylabel = ylabel

    def setGrid(self, grid: bool) -> None:
        self.grid = grid

    def setFigsize(self, figsize: tuple) -> None:
        self.figsize = figsize

    def setXTickFontSize(self, fontSize: int) -> None:
        self.xTickFontSize = fontSize

    def setYTickFontSize(self, fontSize: int) -> None:
        self.yTickFontSize = fontSize

    def setXLim(self, xlim: tuple) -> None:
        self.xlim = xlim

    def setYLim(self, ylim: tuple) -> None:
        self.ylim = ylim

    def setTrendline(self, trendline: Trendline) -> None:
        self.trendlines.append(trendline)

    def setTrendlineInteractive(
        self, trendlineInteractive: TrendlineInteractive
    ) -> None:
        self.trendlineInteractives.append(trendlineInteractive)

    def setLegend(self, legend: Legend) -> None:
        self.legend = legend

    def setSliderHorizontalPadding(self, padding: float) -> None:
        self.sliderHorizontalPadding = padding

    def setSliderVerticalPadding(self, padding: float) -> None:
        self.sliderVerticalPadding = padding

    def setSliderHorizontalBottom(self, bottom: float) -> None:
        self.sliderHorizontalBottom = bottom

    def setSliderVerticalLeft(self, left: float) -> None:
        self.sliderVerticalLeft = left

    def setSliderHorizontalLeft(self, left: float) -> None:
        self.sliderHorizontalLeft = left

    def setSliderVerticalBottom(self, bottom: float) -> None:
        self.sliderVerticalBottom = bottom

    # PRIVATE FUNCTIONS

    def __isAnythingGraphed(self):
        return len(self.trendlines) + len(self.trendlineInteractives) > 0

    def __setFigureLimits(self) -> None:
        if self.xlim is not None:
            self.ax.set_xlim(list(self.xlim))
        elif not self.__isAnythingGraphed():
            self.ax.set_xlim([0, 1])
        else:
            xvalues = np.array(
                [trendline.getX() for trendline in self.trendlines]
                + [trendline.getX() for trendline in self.trendlineInteractives]
            ).flatten()
            xmin = min(xvalues)
            xmax = max(xvalues)
            xrange = xmax - xmin
            self.ax.set_xlim([xmin - xrange / 10, xmax + xrange / 10])

        if self.ylim is not None:
            self.ax.set_ylim(list(self.ylim))
        elif not self.__isAnythingGraphed():
            self.ax.set_ylim([0, 1])
        else:
            yvalues = np.array(
                [trendline.getY() for trendline in self.trendlines]
                + [trendline.getY() for trendline in self.trendlineInteractives]
            ).flatten()
            ymin = min(yvalues)
            ymax = max(yvalues)
            yrange = ymax - ymin
            self.ax.set_ylim([ymin - yrange / 10, ymax + yrange / 10])

    def __setPlotTitles(self) -> None:
        if self.title is not None:
            self.ax.set_title(self.title.getTitle(), fontsize=self.title.getFontSize())
        if self.xlabel is not None:
            self.ax.set_xlabel(
                self.xlabel.getTitle(), fontsize=self.xlabel.getFontSize()
            )
        if self.ylabel is not None:
            self.ax.set_ylabel(
                self.ylabel.getTitle(), fontsize=self.ylabel.getFontSize()
            )

    def __setTickFontSize(self) -> None:
        self.fig.canvas.draw()
        if self.xTickFontSize is not None:
            xlabels = self.ax.get_xticklabels()
            self.ax.set_xticklabels(xlabels, fontsize=self.xTickFontSize)
        if self.yTickFontSize is not None:
            ylabels = self.ax.get_yticklabels()
            self.ax.set_yticklabels(ylabels, fontsize=self.xTickFontSize)

    def __convertColorToTriplet(self, color: Color) -> tuple:
        return (
            None
            if color is None
            else (color.getRed(), color.getGreen(), color.getBlue())
        )

    def __plotTrendlines(self) -> None:
        for trendline in self.trendlines:
            self.ax.plot(
                trendline.getX(),
                trendline.getY(),
                linewidth=trendline.getLineWidth(),
                label=trendline.getName(),
                linestyle=trendline.getLineStyle(),
                marker=trendline.getMarker(),
                color=self.__convertColorToTriplet(trendline.getColor()),
            )

    def __sliderUpdated(self, val) -> None:
        for (
            trendlineInteractive,
            trendlineInteractivePlot,
            trendlineInteractivePlotSlider,
        ) in zip(
            self.trendlineInteractives,
            self.trendlineInteractivePlots,
            self.trendlineInteractivePlotSliders,
        ):
            for i, slider in enumerate(trendlineInteractivePlotSlider):
                trendlineInteractive.getSlider(i).setValue(slider.val)
            trendlineInteractivePlot.set_ydata(trendlineInteractive.getY())

        self.fig.canvas.draw_idle()

    def __plotSlidersAndTextboxes(self) -> None:
        sliders = np.array(
            [
                [slider for slider in trendlineInteractive.getSliders()]
                for trendlineInteractive in self.trendlineInteractives
            ]
        ).flatten()
        textboxes = np.array(
            [
                [textbox for textbox in trendlineInteractive.getTextboxes()]
                for trendlineInteractive in self.trendlineInteractives
            ]
        ).flatten()

        horizontalThickness = sum(
            [
                s.getThickness()
                for s in sliders
                if s.getOrientation() == Orientation.HORIZONTAL
            ]
            +
            [tb.getThickness() for tb in textboxes]
        )
        verticalThickness = sum(
            [
                s.getThickness()
                for s in sliders
                if s.getOrientation() == Orientation.VERTICAL
            ]
        )
        horizontalPos = self.sliderVerticalLeft
        verticalPos = self.sliderHorizontalBottom
        plt.subplots_adjust(
            left=horizontalPos + self.sliderVerticalPadding,
            bottom=verticalPos + self.sliderHorizontalPadding,
        )

        for trendlineInteractive in self.trendlineInteractives:
            plotSliderList = []
            for slider in trendlineInteractive.getSliders():
                thickness = slider.getThickness()
                length = slider.getLength()

                if slider.getOrientation() == Orientation.VERTICAL.value:
                    axSlider = plt.axes(
                        [
                            horizontalPos,
                            self.sliderVerticalBottom,
                            thickness,
                            self.sliderVerticalBottom + length,
                        ],
                        facecolor=self.__convertColorToTriplet(slider.getColor()),
                    )
                    horizontalPos += thickness
                elif slider.getOrientation() == Orientation.HORIZONTAL.value:
                    axSlider = plt.axes(
                        [
                            self.sliderHorizontalLeft,
                            verticalPos,
                            self.sliderHorizontalLeft + length,
                            thickness,
                        ],
                        facecolor=self.__convertColorToTriplet(slider.getColor()),
                    )
                    verticalPos += thickness
                else:
                    raise AssertionError(
                        "Invalid orientation {}", slider.getOrientation()
                    )

                plotSlider = PlotSlider(
                    ax=axSlider,
                    label=slider.getLabel().getTitle(),
                    # fontsize=slider.getLabel().getFontSize(),
                    valmin=slider.getMin(),
                    valmax=slider.getMax(),
                    valinit=slider.getValue(),
                    orientation=slider.getOrientation(),
                    valfmt=slider.getValueFormat()
                )
                plotSlider.label.set_size(slider.getLabel().getFontSize())
                plotSlider.on_changed(self.__sliderUpdated)
                plotSliderList.append(plotSlider)

            self.trendlineInteractivePlotSliders.append(plotSliderList)

    def __plotTrendlineInteractives(self) -> None:
        if len(self.trendlineInteractives) == 0:
            return

        for trendlineInteractive in self.trendlineInteractives:
            trendlineInteractivePlot = self.ax.plot(
                trendlineInteractive.getX(),
                trendlineInteractive.getY(),
                linewidth=trendlineInteractive.getLineWidth(),
                label=trendlineInteractive.getName(),
                linestyle=trendlineInteractive.getLineStyle(),
                marker=trendlineInteractive.getMarker(),
                color=self.__convertColorToTriplet(trendlineInteractive.getColor()),
            )[0]
            self.trendlineInteractivePlots.append(trendlineInteractivePlot)

        self.__plotSlidersAndTextboxes()

    def __putLegend(self) -> None:
        if self.legend is not None:
            self.ax.legend(
                loc=self.legend.getLocation(),
                fontsize=self.legend.getFontSize(),
                ncol=self.legend.getColumnNumber(),
                title=self.legend.getTitle(),
            )

    def __plot_graph(self) -> None:
        self.fig, self.ax = plt.subplots(1, 1, figsize=self.figsize)

        if self.grid:
            self.ax.grid()

        self.__setFigureLimits()
        self.__setPlotTitles()
        self.__setTickFontSize()
        self.__plotTrendlines()
        self.__plotTrendlineInteractives()
        self.__putLegend()

    # PLOTTING FUNCTIONS

    def show(self) -> None:
        self.__plot_graph()
        plt.show()
        plt.close()

    def save(self, address: str) -> None:
        self.__plot_graph()
        plt.savefig(address)
        plt.close()
