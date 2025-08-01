def get_pid(line_arr: list[int], KP: float=0, KI: float=0, KD: float=0) -> int | list:
    """
    This function makes pid values of line error values.
    Arguments:
    line_arr - values of QTR8A/RC
    KP, KI, KD - PID coefficients

    Returns -1 in case of wrong arg type
    Returns -2 in case of len is less than 2
    Returns -3 in case of line_arr values are out of range
    Returns final array in successful case
    """

    if not (isinstance(line_arr, list) and
            (isinstance(KP, float) or isinstance(KP, int)) and
            (isinstance(KI, float) or isinstance(KI, int)) and
            (isinstance(KD, float) or isinstance(KD, int))):
        return -1

    MAX_VALUE = 255
    MIN_VALUE = 0

    integral = 0
    final_arr = []
    lenght = len(line_arr)
    line_arr = get_errors(line_arr)

    if lenght < 2:
        return -2

    if line_arr == -1:
        return -3

    for error_number in range(lenght):
        error = line_arr[error_number]
        res = KP * error + KI * integral + KD * line_arr[error_number-1]
        res = abs(res)
        if res > MAX_VALUE:
            res = MAX_VALUE
        elif res < MIN_VALUE:
            res = MIN_VALUE

        final_arr.append(res)

        integral += error

    return final_arr

def get_errors(line_arr: list[int]) -> int|list:
    """
    This function get errors from QTR8A/RC line values

    Returns -1 in ase of line_arr values are out of range
    Returns final array in successful case
    """
    if len(line_arr) < 1:
        return -1
    if max(line_arr) > 7000 or min(line_arr) < 0:
        return -1

    return list(map(lambda x: x - 3500, line_arr))
