import customtkinter as ctk

class TransparentWidget(ctk.CTkFrame):
    def __init__(
            self,
            master : ctk.CTk | ctk.CTkFrame,
            **kwargs
        ):
        ctk.CTkFrame.__init__(
            self,
            master=master,
            fg_color="transparent",
            **kwargs
        )

    def debug(self):
        self.configure(fg_color="#11ff00")