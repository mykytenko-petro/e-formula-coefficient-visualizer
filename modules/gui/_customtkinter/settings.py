import os

import customtkinter as ctk
from ..palette import color_palette

class Window(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(
            self,
            fg_color=color_palette["primary"]
        )

        self.title("e-formula coefficient visualizer")
        self.iconbitmap(
            os.path.abspath(
                path=os.path.join(
                    __file__,
                    "..", "..", "..", "..",
                    "static", "icons", "icon.ico"
                )
            )
        )
        self.geometry("960x540")

window = Window()