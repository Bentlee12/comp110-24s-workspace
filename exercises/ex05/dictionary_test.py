"""Dictionary Tests for EX05 functions."""

__author__ = "730463172"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_user_case_one() -> None:
    """Inverting keys and Values of UNC Basketball Players."""
    basketball_players_dictionary: dict[str, str] = {'rj': 'davis', 'armando': 'bacot'}
    invert(basketball_players_dictionary)
    assert basketball_players_dictionary == {'davis': 'rj', 'bacot': 'armando'}


def test_invert_user_case_two() -> None: 
    """Inverting Keys and Values of Letters and Fruits."""
    fruit_dictionary: dict[str, str] = {'a': 'apple', 'b': 'banana', 'p': 'plum'}
    invert(fruit_dictionary)
    assert fruit_dictionary == {'apple': 'a', 'banana': 'b', 'plum': 'p'}


def test_invert_edge_case() -> None:
    """Using Empty dictionary."""
    empty_dictionary: dict[str, str] = {"": ""}
    invert(empty_dictionary)
    assert empty_dictionary == {"": ""}


def test_favorite_color_user_case_one() -> None:
    """All people have the same favorite color."""
    color_dict: dict[str, str] = {'Bentlee': 'blue', 'Megan': 'blue', 'Morgan': 'blue'}
    favorite_color(color_dict)
    assert color_dict == 'blue'


def test_favorite_color_user_case_two() -> None:
    """Two people have the same favorite color."""
    color_dict: dict[str, str] = {'Bentlee': 'blue', 'Megan': 'pink', 'Morgan': 'blue'}
    favorite_color(color_dict)
    assert color_dict == 'blue'


def test_favorite_color_edge_case() -> None: 
    """There is a tie for a favorite color."""
    color_dict: dict[str, str] = {'Bentlee': 'blue', 'Megan': 'pink', 'Morgan': 'blue', 'Emily': 'pink'}
    favorite_color(color_dict)
    assert color_dict == 'blue'


def test_count_user_case_one() -> None:
    """Counting number of animals."""
    animals: list[str] = ["cow", "cat", "bird", "cow"]
    count(animals)
    assert animals == {"cow": 2, "cat": 1, "bird": 1}


def test_count_user_case_two() -> None:
    """Counting number of the same animal."""
    animals: list[str] = ["cow", "cow", "cow", "cow", "cow"]
    count(animals)
    assert animals == {"cow": 5}


def test_count_edge_case_() -> None:
    """Counting list with one animal."""
    animals: list[str] = ["cow"]
    count(animals)
    assert animals == {"cow": 1}


def test_alphabetizer_user_case_one() -> None: 
    """Alphabetizing Animals."""
    animals: list[str] = ["bird", "cow", "dog", "donkey", "giraffe"]
    alphabetizer(animals)
    assert animals == {'b': ["bird"], 'c': ["cow"], 'd': ["dog", "donkey"], 'g': ["giraffe"]}


def test_alphabetizer_user_case_two() -> None:
    """Alphabetizing People."""
    people: list[str] = ["Bentlee", "Emily", "Julia", "Megan", "Morgan", "Rylee"]
    alphabetizer(people)
    assert people == {'b': ["Bentlee"], 'e': ["Emily"], 'm': ["Megan", "Morgan"], 'r': ["Rylee"]}


def test_alphabetizer_edge_case() -> None: 
    """You only have one name."""
    people: list[str] = ["Shelley"]
    alphabetizer(people)
    assert people == {'s': ["Shelley"]}


def test_update_attendance_test_user_case_one() -> None:
    """Adding Student to Day of Week that Already Exists."""
    current_attendance: dict[str, list[str]] = {"Monday": ["Bentlee", "Rylee"], "Tuesday": ["Megan", "Emily"], "Wednesday": ["Bentlee"]}
    update_attendance(current_attendance, "Monday", "Emily")
    assert current_attendance == {"Monday": ["Bentlee", "Rylee", "Emily"], "Tuesday": ["Megan", "Emily"], "Wednesday": ["Bentlee"]}


def test_update_attendance_test_user_case_two() -> None: 
    """Adding Student to New Day of the Week."""
    current_attendance: dict[str, list[str]] = {"Monday": ["Bentlee", "Rylee"], "Tuesday": ["Megan", "Emily"], "Wednesday": ["Bentlee"]}
    update_attendance(current_attendance, "Thursday", "Emily")
    assert current_attendance == current_attendance == {"Monday": ["Bentlee", "Rylee"], "Tuesday": ["Megan", "Emily"], "Wednesday": ["Bentlee"], "Thursday": ["Emily"]}


def test_update_attendance_edge_case() -> None:
    """Adding Day of Week to Empty Attendance."""
    current_attendance: dict[str, list[str]] = {}
    update_attendance(current_attendance, "Monday", "Emily")
    assert current_attendance == {"Monday": ["Emily"]}

    