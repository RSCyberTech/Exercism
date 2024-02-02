def reverse(text):
    if len(text) > 0:
        text = list(text)
        text.reverse()
        ret = ""
        for t in text:
            ret += t
        return ret
    else:
        return ""
