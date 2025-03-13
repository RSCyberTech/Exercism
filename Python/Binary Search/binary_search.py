def find(search_list, value):
    lowerPosition = 0
    while len(search_list) > 1:
        if value < search_list[int(len(search_list) / 2)]:
            search_list = search_list[: int(len(search_list) / 2)]
        elif value >= search_list[int(len(search_list) / 2)]:
            lowerPosition += int(len(search_list) / 2)
            search_list = search_list[int(len(search_list) / 2) :]
        else:
            raise ValueError("value not in array")

    if len(search_list) < 1 or value != search_list[0]:
        raise ValueError("value not in array")
    return lowerPosition
