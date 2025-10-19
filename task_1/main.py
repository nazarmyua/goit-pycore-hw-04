from data import get_data
from processing import process_data


def total_salary(path) -> tuple[int, int] | None:
    data = get_data(path)
    statistic = process_data(data)
    return statistic
