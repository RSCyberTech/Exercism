def value(colors):
    d = {
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
    return int(str(d[colors[0].capitalize()]) + str(d[colors[1].capitalize()]))
