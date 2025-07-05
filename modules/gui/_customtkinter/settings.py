import os

import customtkinter as ctk
from tkinter import PhotoImage
from ..palette import color_palette

class Window(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(
            self,
            fg_color=color_palette["primary"]
        )
        self.iconphoto(True, PhotoImage(
            file=os.path.abspath(path=os.path.join(
                __file__, "..", "..", "..", "..",
                "static", "icons", "icon.png"
                    )
                )
            )
        )
        self.title("e-formula coefficient visualizer")
        self.geometry("960x540")

window = Window()
