def flatten(iterable):
    toReturn = []
    for i in iterable:
        if type(i) != list and i != None:
            toReturn.append(i)
        elif type(i) == list:
            toReturn += flatten(i)

    return toReturn
