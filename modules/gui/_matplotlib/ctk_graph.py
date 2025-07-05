import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk

class CTkGraph(ctk.CTkFrame):
    def __init__(
            self,
            master : ctk.CTkBaseClass,
            **kwargs
        ):

        ctk.CTkFrame.__init__(
            self,
            master=master,
            **kwargs
        )

        self.pack_propagate(False)

        fig, ax = plt.subplots()
        self._figure_canvas = FigureCanvasTkAgg(
            figure=fig,
            master=self
        )
        self._figure_canvas.get_tk_widget().pack(
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

    def plot(self):
        self._figure_canvas.draw()