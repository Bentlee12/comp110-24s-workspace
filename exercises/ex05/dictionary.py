"""Dictionary Utility Function."""

__author__ = "730463172"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting Keys and Values."""
    returndict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in returndict:
            raise KeyError("Same value encountered more than once.")
        returndict[dictionary[key]] = key
    return (returndict)


def favorite_color(dictionary2: dict[str, str]) -> str:
    """Returning Favorite Color."""
    color_idx: str = ""
    counter: int = 0
    while counter < len(dictionary2):
        if dictionary2[counter] < dictionary2[color_idx]:
            color_idx = dictionary2[color_idx]
        counter += 1
    return color_idx


def count(countlist: list[str]) -> dict[str, int]:
    """Returning Count."""


def alphabetizer(alphabet: list[str]) -> dict[str, list[str]]:
    """Alphabetizing."""
    
    
def update_attendance(attendance: dict[str, list[str]], weekday: str, student: str) -> None:
    """Updating Attendence."""