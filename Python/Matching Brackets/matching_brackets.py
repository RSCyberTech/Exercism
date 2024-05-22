def is_paired(input_string):
    pairs = {"[": "]", "{": "}", "(": ")"}
    stack = []
    for i in input_string:
        if i in pairs.values():
            if len(stack) == 0:
                return False
            elif pairs[stack.pop(-1)] != i:
                return False
        elif i in pairs.keys():
            stack.append(i)
    if len(stack) != 0:
        return False
    return True
