"""Some functions for my garden plan!"""

__author__ = "730463172"


def add_by_kind(plants_by_kind: dict[str, list[str]], plant_kind: str, plant: str) -> None:
    """Adding plant by kind."""
    if plant_kind in plants_by_kind:
        plants_by_kind[plant_kind].append(plant)
    else:
        plants_by_kind[plant_kind] = []
        plants_by_kind[plant_kind].append(plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Adding Plants by Date."""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], plant_kind: str, month: str) -> str:
    """Lookup Plants by Kind and Date."""
    combined: list[str] = []
    if plant_kind in plants_by_kind and month in plants_by_date:
        for plant in plants_by_kind[plant_kind]:
            if plant in plants_by_date[month]: 
                combined.append(plant)
    else:
        return f"no {plant_kind}s to plant in {month} "
    if len(combined) > 0: 
        return f"{plant_kind}s to plant in {month}: {combined}"
    else:
        return f"no {plant_kind}s to plant in {month} "
    