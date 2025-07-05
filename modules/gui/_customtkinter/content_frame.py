import customtkinter as ctk

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


contentFrame = ContentFrame()
contentFrame.pack(
    expand=True,
    anchor=ctk.CENTER 
)
contentFrame.debug()