from typing import TypedDict

class CoefficientPayload(TypedDict):
    Kp: int
    Ki: int
    Kd: int