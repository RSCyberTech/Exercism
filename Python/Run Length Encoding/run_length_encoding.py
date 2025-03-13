import re


def decode(string):
    return "".join(
        [
            int(r[:-1]) * r[-1] if len(r) > 1 else r[0]
            for r in re.findall(r"([0-9]*[^0-9]{1})", string)
        ]
    )


def encode(string):
    if len(string) == 0:
        return ""
    out = [string[0]]
    for s in string[1:]:
        if s == out[-1][0]:
            out[-1] = out[-1] + s
        else:
            out.append(s)

    return "".join([str(len(o)) + o[0] if len(o) > 1 else o for o in out])
