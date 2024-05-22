def translate(text):
    phrase = text.split(" ")
    for r in range(len(phrase)):
        p = phrase[r]
        if p.startswith("xr") or p.startswith("yt"):
            pass
        elif p.startswith("ch") or p.startswith("st"):
            p = p[2:] + text[0:2]
        elif p[0] in "bcdfghjklmnpqrstvwxyz" and p[1:3] == "qu":
            p = p[3:] + p[:3]
        elif p[0:2] == "qu":
            p = p[2:] + p[0:2]
        elif p[0] in "bcdfghjklmnpqrstvwxyz":
            newWord = p[1:] + p[0]
            p = newWord
            for t in newWord:
                if t in "bcdfghjklmnpqrstvwxz":
                    newWord = p[1:] + p[0]
                    p = newWord
                else:
                    break
        phrase[r] = p + "ay"

    return " ".join(phrase)
