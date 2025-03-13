import math


def cipher_text(plain_text):
    plain_text = "".join([p for p in plain_text.lower() if p.isalnum()])

    c = r + 1 if len(plain_text) > (r := int(math.sqrt(len(plain_text)))) ** 2 else r

    lists = [[] for _ in range(c)]

    for r in range(len(plain_text)):
        lists[r % c].append(plain_text[r])

    lists = " ".join([("".join(l)) + (" " * (len(lists[0]) - len(l))) for l in lists])

    return lists
