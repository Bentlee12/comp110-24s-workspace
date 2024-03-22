"""Pratcice w Dictionaries for for Loops."""

in_stock: dict[str,bool]= {"carrots=": True, "beets":False, "apples": True}

#print out the keys that have True values
for key in in_stock:
    # key is going to be "carrots", "beets", "apples"
    # in_stock[key] is going to be True, False, True 
    print(key)
    value: bool= in_stock[key]
    print(value)
    if in_stock[key] is True:
        print(key)







        