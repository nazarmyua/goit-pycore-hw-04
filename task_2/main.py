from data import get_data
from parser import parse_cats_data

def get_cats_info(path) -> list[dict]:
    cats_info = get_data(path)
    return parse_cats_data(cats_info)