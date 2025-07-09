import json

def read_json(path : str) -> dict:
    with open(file=path, encoding='utf-8', mode='r') as file:
        return json.load(file)
    
def write_json(path : str, data : dict) -> None:
    with open(file=path, encoding='utf-8', mode='w') as file:
        return json.dump(data, file, indent = 4)
    
def update_json(path : str, data : dict) -> None:
    data_to_modify = read_json(path=path)
    data_to_modify.update(data)
    
    write_json(path=path, data=data_to_modify)