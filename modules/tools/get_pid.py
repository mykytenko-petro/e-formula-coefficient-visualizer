from exceptions import *

def get_pid(line_arr: list[int], KP: float=0, KI: float=0, KD: float=0):
    """
    This function makes pid values of line error values.
    Arguments:
    line_arr - values of QTR8A/RC
    KP, KI, KD - PID coefficients
    """
    integral = 0
    final_arr = []
    lenght = len(line_arr)

    if lenght < 2:
        raise TooSmallArrayError()

    for error_n in range(1, lenght):
        error = line_arr[error_n]
        res = KP * error + KI * integral + KD * line_arr[error_n-1]
        final_arr.append(res)

        integral += error

    return final_arr

def get_errors(line_arr: list[int]):
    """
    This function get errors from QTR8A/RC line values
    """
    if max(line_arr) > 7000 or min(line_arr) < 0:
        raise ValueOutOfRangeError()

    return list(map(lambda x: x - 3500, line_arr))
