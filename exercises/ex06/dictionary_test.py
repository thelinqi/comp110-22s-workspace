"""My dictionary exericise test!"""

__author__ = "730487849"


from dictionary import invert, favorite_color, count
import pytest


def test_invert() -> None:
    """Testing the invert function."""
    og_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(og_dict) == {"z": "a", "y": "b", "x": "c"}


def test_invert_2() -> None:
    """Testing the invert function."""
    og_dict: dict[str, str] = {"apple": "cat", "banana": "dog"}
    assert invert(og_dict) == {"cat": "apple", "dog": "banana"}


def test_invert_keyerror() -> None:
    """Testing the invert function."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color() -> None:
    """Testing the favorite color function."""
    og_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Lin": "blue"}
    assert favorite_color(og_dict) == "blue"


def test_favorite_color_2() -> None:
    """Testing the favorite color function."""
    og_dict: dict[str, str] = {"Lin": "blue", "Jasper": "green"}
    assert favorite_color(og_dict) == "blue"


def test_favorite_color_3() -> None:
    """Testing the favorite color function."""
    og_dict: dict[str, str] = {"Jasper": "red", "Erin": "yellow", "Lyle": "yellow"}
    assert favorite_color(og_dict) == "yellow"


def test_count() -> None:
    """Testing the count function."""
    og_list: list[str] = ["cat", "pig", "pig", "cat", "dog"]
    assert count(og_list) == {"cat": 2, "pig": 2, "dog": 1}


def test_count_2() -> None:
    """Testing the count function."""
    og_list: list[str] = ["happy", "happy", "sad", "sad", "emo"]
    assert count(og_list) == {"happy": 2, "sad": 2, "emo": 1}


def test_count_3() -> None:
    """Testing the count function."""
    og_list: list[str] = ["emo"]
    assert count(og_list) == {"emo": 1}
