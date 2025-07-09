def read_txt(path : str) -> str:
    with open(file=path, encoding="utf8", mode="r") as file:
        return file.read()
    
def txt_str_to_int(
        path : str,
        split_by : str = ","
    ) -> list[int]:

    txt = read_txt(path)

    str_list = txt.split(split_by)

    int_list = []
    for value in str_list:
        int_list.append(int(value))

    return int_list