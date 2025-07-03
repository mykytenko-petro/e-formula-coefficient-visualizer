from exceptions import *

def get_pid(line_arr: list[int], KP: float, KD: float):
    final_arr = []
    lenght = len(line_arr)

    if lenght < 2:
        raise TooSmallArrayError()

    for i in range(1, lenght):
        pos = line_arr[i]
        res = KP * pos + KD * line_arr[i-1]
        final_arr.append(res)

    return final_arr

