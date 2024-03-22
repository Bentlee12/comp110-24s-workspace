"""Splitting a dictionary into two lists."""
__author__ = "730463172"

 
def get_keys(input: dict[str, int]) -> list[str]:
    """Producing List of Keys."""
    keylist: list[str] = []
    for keys in input:
        keylist.append(keys)
        return (keylist)    
    return keylist
    

def get_values(input2: dict[str, int]) -> list[int]:
    """Getting List Values."""
    valuelist: list[int] = []
    for keys in input2:
        valuelist.append(input2[keys])
        return (valuelist)
    return valuelist
