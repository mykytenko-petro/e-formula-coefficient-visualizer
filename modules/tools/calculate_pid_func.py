import os

from ..utils import read_json, read_txt
from .get_pid import get_pid
from .types import CoefficientPayload

def calculate_pid() -> list | None:
    coefficients: CoefficientPayload = read_json(
        path=os.path.abspath(
            path=os.path.join(
                __file__,
                "..", "..", "..",
                "json", "coefficients.json"
            )
        )
    )

    raw_line_value_list = read_txt(
        path=os.path.abspath(
            path=os.path.join(
                __file__,
                "..", "..", "..",
                "txt", "way.txt"
            )
        )
    ).split(",")

    line_value_list: list[int] = []
    for value in raw_line_value_list:
        line_value_list.append(int(value))

    pid_value_list = get_pid(
        line_arr=line_value_list,
        KP=coefficients["Kp"],
        KI=coefficients["Ki"],
        KD=coefficients["Kd"]
    )

    if isinstance(pid_value_list, list):
        return pid_value_list
    else:
        print(pid_value_list)