def answer(question):
    operators = {
        "plus": "+",
        "minus": "-",
        "multiplied": "*",
        "divided": "/",
    }

    for k, v in operators.items():
        question = question.replace(k, v)
    question = (
        question.replace("What", "")
        .replace("is", "")
        .replace("?", "")
        .replace("by", "")
        .strip()
        .split()
    )

    if len(question) == 0:
        raise ValueError("syntax error")

    while len(question) > 1:

        if question[1] not in operators.values():
            if question[1].isdigit() == False:
                raise ValueError("unknown operation")
            else:
                raise ValueError("syntax error")

        try:
            n1 = int(question[0])
        except:
            raise ValueError("syntax error")

        try:
            n2 = int(question[2])
        except:
            raise ValueError("syntax error")

        r = eval(str(n1) + question[1] + str(n2))
        question = [str(int(r))] + question[3:]

    return int(question[0])
