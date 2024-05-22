import math


def rebase(input_base, digits, output_base):

    # filter invalids
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    elif output_base < 2:
        raise ValueError("output base must be >= 2")

    for d in digits:
        if not 0 <= d < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # convert to decimal
    for r in range(len(digits) - 1, -1, -1):
        if digits[r] == 0:
            continue
        digits[r] = int(digits[r] * (math.pow(input_base, (len(digits) - 1 - r))))
    s = sum(digits)

    # convert to intended base
    digits = []
    toCheck = [1, output_base]
    while (toAdd := toCheck[-1] * output_base) < s:
        toCheck.append(toAdd)
    toCheck.reverse()

    remainder = 0
    for digit in toCheck:
        digits.append(int(s // digit))
        s = s % digit

    # remove leading zeros
    for r in range(len(digits) - 1):
        if digits[r] == 0:
            del digits[r]
        else:
            break

    return digits
