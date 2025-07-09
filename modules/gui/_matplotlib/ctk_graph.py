import customtkinter as ctk
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class CTkGraph(ctk.CTkFrame):
    def __init__(
            self,
            master : ctk.CTkBaseClass,
            title : str = "",
            xlabel : str = "",
            ylabel : str = "",
            **kwargs
        ):

        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel

        ctk.CTkFrame.__init__(
            self,
            master=master,
            **kwargs
        )

        self.pack_propagate(False)

        # matplotlib part
        self._fig = Figure()
        self._ax = self._fig.add_subplot()

        # tkinter part
        self._figure_canvas = FigureCanvasTkAgg(
            figure=self._fig,
            master=self
        )

        self.figure_widget = self._figure_canvas.get_tk_widget()
        self.figure_widget.pack(
            side=ctk.TOP,
            fill=ctk.BOTH,
            expand=True
        )

        self._navigation_tool_bar = NavigationToolbar2Tk(
            canvas=self._figure_canvas,
            window=self
        )
        self._navigation_tool_bar.pack(
            side=ctk.TOP,
        )

        self.plot()

    def plot(
            self,
            x_axis : list | None = None,
            y_axis : list | None = None
        ):
        self._ax.clear()

        self._ax.set_title(self.title)
        self._ax.set_xlabel(self.xlabel)
        self._ax.set_ylabel(self.ylabel)

        self._ax.plot(
            numpy.array(y_axis),
            numpy.array(x_axis),
            'o',
            color="r" 
        )

        self._figure_canvas.draw()