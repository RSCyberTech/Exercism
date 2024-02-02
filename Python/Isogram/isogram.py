def is_isogram(string):
    d = []
    for s in string:
        if s == " " or s == "-":
            continue
        if s.lower() in d:
            return False
        else:
            d.append(s.lower())
    return True
