import os

import customtkinter as ctk

from .settings import window, color_palette
from ...utils import read_json, update_json


def get_coefficients_path() -> str:
    return os.path.abspath(
        os.path.join(
            __file__,
            "..", "..", "..", "..",
            "json", "coefficients.json"
        )
    )


class ValueHolderWidget(ctk.CTkFrame):
    def __init__(
        self,
        master : ctk.CTkScrollableFrame,
        value_name : str
    ):
        ctk.CTkFrame.__init__(
            self,
            master=master,
            width=200,
            height=50,
            fg_color=color_palette["primary"],
        )
        self.pack_propagate(False)

        self.value_name = value_name
        self.render()

    def render(self):
        for widget in self.pack_slaves():
            widget.pack_forget()

        list_of_coefficients: dict[str, float] = read_json(
            path=get_coefficients_path()
        )

        self.value_var = ctk.Variable(
            value=list_of_coefficients[self.value_name]
        )

        self.value_label = ctk.CTkLabel(
            master=self,
            text=self.value_name,
            text_color=color_palette["text"]
        )
        self.value_label.pack(
            side=ctk.LEFT,
            padx=10
        )

        self.apply_button = ctk.CTkButton(
            master=self,
            width=20,
            fg_color=color_palette["primary"],
            hover_color=color_palette["secondary"],
            text="apply",
            text_color=color_palette["text"],
            command=self.update_value
        )
        self.apply_button.pack(
            side=ctk.RIGHT,
            padx=10
        )

        self.value_holder = ctk.CTkEntry(
            master=self,
            width=50,
            placeholder_text=self.value_var.get(),
            textvariable=self.value_var
        )
        self.value_holder.pack(
            side=ctk.RIGHT
        )

    def update_value(self):
        update_json(
            path=get_coefficients_path(),
            data={self.value_name: float(self.value_var.get())}
        )
        self.render()


class ValueTab(ctk.CTkScrollableFrame):
    def __init__(self):
        ctk.CTkScrollableFrame.__init__(
            self,
            master=window,
            fg_color=color_palette["secondary"],
            width=250,
            corner_radius=0,
            scrollbar_button_color=color_palette["secondary"],
            scrollbar_button_hover_color=color_palette["hover"]
        )

        list_of_coefficients = read_json(
            path=get_coefficients_path()
        ).keys()

        for coefficient in list_of_coefficients:
            self.kd_value_holder = ValueHolderWidget(
                master=self,
                value_name=coefficient
            )
            self.kd_value_holder.pack(
                pady=10
            )

valueTab = ValueTab()
valueTab.pack(
    fill="y",
    side=ctk.LEFT
)