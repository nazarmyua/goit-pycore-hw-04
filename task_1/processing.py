def process_data(data: list[str]) -> tuple[int, int] | None:
    salaries = get_salaries(data)

    if not salaries:
        return None

    salaries_sum = sum(salaries)
    return (salaries_sum, salaries_sum / len(salaries))


def get_salaries(data: list[str]) -> list[float]:
    result = []
    for item in data:
        try:
            result.append(float(item.split(",")[1].strip()))
        except Exception as ex:
            print(f"file corrupted. line: {item}. Original error: {ex}")
            return []

    return result
