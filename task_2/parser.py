def parse_cats_data(data: list[str]) -> list[dict]:
    result = []
    for item in data:
        try:
            cat = item.split(",")
            result.append({"id": cat[0].strip(), "name": cat[1].strip(), "age": cat[2].strip()})
        except Exception as ex:
            print(f"Failed to parse the line: {item}. Original exeption: {ex}")
            continue

    return result
