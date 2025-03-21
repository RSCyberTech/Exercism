def roman(number):
    r = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    out = ""
    for k in r.keys():
        while number >= k:
            out += r[k]
            number -= k
    return out
