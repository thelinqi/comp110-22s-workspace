"""Utility functions."""

__author__ = "730487849"


def only_evens(xs: list[int]) -> list[int]:
    """Returns the even integers in the list."""
    i: int = 0
    final: list[int] = []
    while i < len(xs):
        if xs[i] % 2 == 0:
            final.append(xs[i])
        i += 1
    return final


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Returns a list which is a subset of the given list."""
    final: list[int] = list()
    if len(xs) == 0:
        return final
    if a < 0: 
        a = 0
    if b > len(xs) - 1:
        b = len(xs)

    i: int = a
    while i < b:
        final.append(xs[i])
        i += 1
    return final


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Combining two lists."""
    for item in b_list:
        a_list.append(item)
    return a_list