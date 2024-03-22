"""Ex04 Utils."""
__author__ = "730463172"


def all(num1: list[int], input1: int) -> bool:
    """All Function."""
    counter: int = 0
    results: bool = True
    if len(num1) == 0:
        results = False   
        counter = len(num1)  
    while counter < len(num1):
        if num1[counter] == input1:
            results = True
        elif num1[counter] != input1:
            counter = len(num1)
            results = False
        counter += 1
    return results


print(all)


def max(input: list[int]) -> int:
    """Returning Max."""
    listcounter: int = 0
    maxnumber = int(input[0])
    length: int = int(len(input))
    if len(input) == 0:
        raise ValueError("max() arg is an empty List ")
    while listcounter < length:
        if input[listcounter] > maxnumber:
            maxnumber = input[listcounter]
        listcounter += 1
    else:
        listcounter += 1
    return (maxnumber)


print(max)


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Checking for Equality."""
    results: bool = True
    if len(input1) and len(input2) == 0:
        results = True
    if len(input1) or len(input2) == 0:
        results = False
    if len(input1) != len(input2):
        results = False
    if len(input1) == len(input2) and input1 != input2:
        results = False
    return (results)
        

def extend(input1: list[int], input2: list[int]) -> None:
    """Extending List."""
    for elems in input2:
        input1.append(input2[elems])
    counter: int = 0
    input2elems: int = 0
    while counter < len(input2):
        input2elems += input2[counter]
        counter += 1
    input1.append(input2elems)

        