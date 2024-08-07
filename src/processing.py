input_data: list[dict[str, str | int]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(
    list_of_dictionaries_state: list[dict[str, str | int]], state: str = "EXECUTED"
) -> list[dict[str, str | int]]:
    """Функция возвращает список словарей в которых состояние равно заданному значению"""
    result_list_dict = []
    for i in range(len(list_of_dictionaries_state)):
        if list_of_dictionaries_state[i]["state"] == state:
            result_list_dict.append(list_of_dictionaries_state[i])
        else:
            continue
    return result_list_dict


# print(filter_by_state(input_data, state ='CANCELED'))
print(filter_by_state(input_data))
