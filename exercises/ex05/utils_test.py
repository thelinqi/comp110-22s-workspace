"""Testing my utility functions."""

__author__ = "730487849"


from utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Testing the only_evens function."""
    xs: list[int] = [2, 4, 10]
    assert only_evens(xs) == [2, 4, 10]


def test_sub() -> None:
    """Testing the sub function."""
    xs: list[int] = [10, 20, 30, 40]
    a: int = 1
    b: int = 3
    assert sub(xs, a, b) == [20, 30]


def test_concat() -> None:
    """Testing the concat function."""
    a_list: list[int] = [1, 3, 8]
    b_list: list[int] = [8, 9, 10]
    assert concat(a_list, b_list) == [1, 3, 8, 8, 9, 10]