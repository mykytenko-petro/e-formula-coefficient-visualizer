from typing import TypedDict

class Palette(TypedDict):
    primary: str
    secondary: str
    border: str
    hover: str
    text: str

color_palette: Palette = {
    "primary": "#a82c36",
    "secondary": "#c23440",
    "border": "#dd9196",
    "hover": "#d03a47",
    "text": "#ffffff",
}