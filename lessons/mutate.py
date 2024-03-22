"""Mutating functions."""

__author__ = "730463172"


def manual_append(a: list[int], b: int) -> None:
    """Appending List."""
    a.append(b)


def double(c: list[int]) -> None:
    """Doubling C."""
    counter = 0
    while int(counter) <= len(c) - 1:
        c[counter] *= 2
        counter += 1
        