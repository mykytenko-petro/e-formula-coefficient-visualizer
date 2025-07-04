from modules.exceptions import ValueOutOfRangeError, TooSmallArrayError

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

def get_errors(line_arr: list[int]):
    if max(line_arr) > 7000 or min(line_arr) < 0:
        raise ValueOutOfRangeError()

    return list(map(lambda x: x - 3500, line_arr))

arr = [0, 7000, 3500]
print(get_errors(arr))
