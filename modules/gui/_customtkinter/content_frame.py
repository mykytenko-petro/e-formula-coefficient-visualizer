import os
import customtkinter as ctk

from ...tools import calculate_pid
from ...utils import txt_str_to_int
from .._matplotlib import CTkGraph
from ..palette import color_palette
from .widgets import TransparentWidget
from .settings import window

def plot_pid_values(graph : CTkGraph):
    pid_list = calculate_pid()

    raw_line_value_list = txt_str_to_int(
        path=os.path.abspath(
            path=os.path.join(
                __file__,
                "..", "..", "..", "..",
                "txt", "way.txt"
            )
        )
    )

    graph.plot(
        x_axis=raw_line_value_list,
        y_axis=pid_list
    )

class ContentFrame(TransparentWidget):
    def __init__(
            self,
        ):

        TransparentWidget.__init__(
            self,
            master=window
        )

        self.graph = CTkGraph(
            master=self,
            width=900,
            height=650,
            title="delta speed/qtr8 values graph",
            xlabel="delta speed",
            ylabel="qtr8 values"
        )

        self.graph.pack(
            expand=True,
            anchor=ctk.CENTER
        )

        self.plot_button = ctk.CTkButton(
            master=self,
            width=20,
            fg_color=color_palette["primary"],
            hover_color=color_palette["secondary"],
            text="plot result",
            text_color=color_palette["text"],
            command=lambda: plot_pid_values(graph= self.graph)
        )

        self.plot_button.pack(
            pady=10,
            anchor=ctk.CENTER
        )


contentFrame = ContentFrame()
contentFrame.pack(
    expand=True,
    anchor=ctk.CENTER 
)
# contentFrame.debug()