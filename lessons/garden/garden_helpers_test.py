"""Test my garden functions."""

__author__ = "730463172"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_user_case() -> None:
    """Testing adding plant by kind."""
    test_dictionary: dict[str, list[str]] = {"flower": ["rose", "sunflower", "peony"], "tree": ["pear", "pine", "apple", "spruce"]}
    add_by_kind(test_dictionary, "flower", "lilly")
    assert test_dictionary == {'flower': ["rose", "sunflower", "peony", "lilly"], 'tree': ["pear", "pine", "apple", "spruce"]}


def test_add_by_kind_edge_case() -> None:
    """Testing adding plant by kind with new category."""
    test_dictionary: dict[str, list[str]] = {"flower": ["rose", "sunflower", "peony"], "tree": ["pear", "pine", "apple", "spruce"]}
    add_by_kind(test_dictionary, "fruit", "strawberry")
    assert test_dictionary == {'flower': ["rose", "sunflower", "peony"], 'tree': ["pear", "pine", "apple", "spruce"], 'fruit': ["strawberry"]}

    
def test_add_by_date_user_case() -> None:
    """Sorting Plants by Date."""
    date_dictionary: dict[str, list[str]] = {"June": ["cucumbers"], "July": ["Watermelon"]}
    add_by_date(date_dictionary, "July", "strawberry")
    assert date_dictionary == {"June": ["cucumbers"], "July": ["Watermelon", "strawberry"]}


def test_add_by_date_edge_case() -> None:
    """Sorting Plants by date with new category."""
    date_dictionary: dict[str, list[str]] = {"June": ["cucumbers"], "July": ["Watermelon"]}
    add_by_date(date_dictionary, "April", "corn")
    assert date_dictionary == {"April": ["corn"], "June": ["cucumbers"], "July": ["Watermelon"]}


def test_lookup_by_kind_date_user_case() -> None:
    """Finding Plants by Kind and Date."""
    by_kind_dictionary: dict[str, list[str]] = {'flower': ["rose", "sunflower", "peony"], 'tree': ["pear", "pine", "apple", "spruce"], 'fruit': ["strawberry"]}
    by_date_dictionary: dict[str, list[str]] = {"April": ["rose", "sunflower", "strawberry", "pear"], "May": ['peony', 'apple', 'pine', 'spruce']}
    combination = lookup_by_kind_and_date(by_kind_dictionary, by_date_dictionary, "fruit", "April")
    assert combination == "fruits to plant in April: ['strawberry']"


def test_lookup_by_kind_date_edge_case() -> None:
    """Finding Plants by Kind and Date with new category."""
    by_kind_dictionary: dict[str, list[str]] = {}
    by_date_dictionary: dict[str, list[str]] = {}
    combination = lookup_by_kind_and_date(by_kind_dictionary, by_date_dictionary, "flower", "April")
    assert combination == "no flowers to plant in April "


