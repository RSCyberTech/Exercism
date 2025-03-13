def abbreviate(words):
    s = words
    for w in words:
        if (not (ord(w.upper()) in range(65, ord("Z") + 1))) and w != " " and w != "'":
            s = words.replace(w, " ")
    return "".join(l[0].upper() for l in s.split())
