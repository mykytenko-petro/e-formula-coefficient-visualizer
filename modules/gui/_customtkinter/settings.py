import os
import sys

import customtkinter as ctk
from tkinter import PhotoImage

from ..palette import color_palette

class Window(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(
            self,
            fg_color=color_palette["primary"]
        )

        self.protocol("WM_DELETE_WINDOW", self._on_exit)

        self.title("e-formula coefficient visualizer")    
        if os.name == "nt":
            self.iconbitmap(
                bitmap=os.path.abspath(
                    path=os.path.join(
                        __file__,
                        "..", "..", "..", "..",
                        "static", "icons", "icon.ico"
                    )
                )
            )
        elif os.name == "posix":
            self.iconphoto(True, PhotoImage(
                file=os.path.abspath(
                    path=os.path.join(
                        __file__,
                        "..", "..", "..", "..",
                        "static", "icons", "icon.png"
                        )
                    )
                )
            )
        self.geometry("960x540")

    def _on_exit(self):
        sys.exit()

window = Window()