"""Summing the elements of a list using different loops."""

# 1: Part 1. Using While Loop 


def w_sum(vals: list[float]) -> float:
    """Return Sum w While Loop."""
    counter: int = 0
    valscounter: float = 0.0
    while counter < len(vals):
        valscounter += vals[counter]
        counter += 1
    return (valscounter)


# 2: Part 2. For Loop 
def f_sum(vals: list[float]) -> float:
    """Return Sum w For Loop."""
    valscounter2: float = 0
    for elems in vals:
        valscounter2 += elems
    return (valscounter2)


# 3: part 3. 
def f_range_sum(vals: list[float]) -> float:
    """Using Range."""
    valscounter3: float = 0
    for nums in range(0, len(vals)):
        valscounter3 += vals[nums]
    return (valscounter3)

        

        
