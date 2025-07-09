import os

import customtkinter as ctk

from ...utils import read_txt
from .._matplotlib import CTkGraph
from ..palette import color_palette
from .widgets import TransparentWidget
from .settings import window

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
            width=650,
            height=500
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
            command=lambda: self.graph.plot(
                first_axis=read_txt(
                    path=os.path.abspath(
                        path=os.path.join(
                            __file__,
                            "..", "..", "..", "..",
                            "txt", "way.txt"
                        )
                    )
                ).split(sep=","),
                second_axis=read_txt(
                    path=os.path.abspath(
                        path=os.path.join(
                            __file__,
                            "..", "..", "..", "..",
                            "txt", "way.txt"
                        )
                    )
                ).split(sep=",")
            )
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