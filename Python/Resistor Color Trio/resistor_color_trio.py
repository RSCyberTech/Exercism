def label(colors):
    codes = {
        "Black": 0,
        "Brown": 1,
        "Red": 2,
        "Orange": 3,
        "Yellow": 4,
        "Green": 5,
        "Blue": 6,
        "Violet": 7,
        "Grey": 8,
        "White": 9,
    }

    toRet = ""
    for c in colors[:2]:
        toRet += str(codes[c.capitalize()])

    if len(colors) > 2:
        toRet += "0" * codes[colors[2].capitalize()]

    if toRet.endswith("000000000"):
        toRet = toRet[:-9] + " gigaohms"
    elif toRet.endswith("000000"):
        toRet = toRet[:-6] + " megaohms"
    elif toRet.endswith("000"):
        toRet = toRet[:-3] + " kiloohms"
    else:
        toRet = str(int(toRet)) + " ohms"

    return toRet
