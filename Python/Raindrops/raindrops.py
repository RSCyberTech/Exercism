def convert(number):

    val = {
        3: "Pling",
        5: "Plang",
        7: "Plong",
    }

    toRet = ""
    for k, v in val.items():
        toRet += v if number % k == 0 else ""

    return toRet if toRet != "" else str(number)
