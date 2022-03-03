"""My dictionary exericise!"""

__author__ = "730487849"


def invert(og_dict: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and the values."""
    result: dict[str, str] = {}
    for key in og_dict:
        value = og_dict[key]
        if value not in result:
            result[value] = key
        else:
            raise KeyError("Cannot have two of the same key.")
    return result


def favorite_color(og_dict: dict[str, str]) -> str:
    """Gives someone's favorite color."""
    new_dict: dict[str, int] = {}
    result: str = ""
    for key in og_dict:
        color_value = og_dict[key]
        if color_value not in new_dict:
            new_dict[color_value] = 1
        else:
            new_dict[color_value] += 1
    i: int = 0
    for key in new_dict:
        if new_dict[key] > i:
            i = new_dict[key]
            result = key
    return result

    
def count(og_list: list[str]) -> dict[str, int]:
    """Counting the values in the input list."""
    new_dict: dict[str, int] = {}
    for key in og_list:
        if key not in new_dict:
            new_dict[key] = 1
        else:
            new_dict[key] += 1
    return new_dict
