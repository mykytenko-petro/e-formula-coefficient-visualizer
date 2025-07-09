def read_txt(path : str) -> str:
    with open(file=path, encoding="utf8", mode="r") as file:
        return file.read()