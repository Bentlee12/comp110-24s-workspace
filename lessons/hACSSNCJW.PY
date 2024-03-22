def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverting Keys and Values."""
    keylist: str = ""
    valuelist: str = ""
    for elems in dictionary:
        if elems[keylist] == elems:
            raise KeyError("KeyError")
        keylist += elems
        valuelist += elems[dictionary]
    return (dict[valuelist,keylist])



keylist: str = ""
    valuelist: str = ""
    emptydict: dict= {valuelist, keylist}
    for elems in dictionary:
        if elems[keylist] == emptydict:
            raise KeyError("KeyError")
        else:
            keylist += elems
            valuelist += elems[dictionary]
    return (emptydict)  