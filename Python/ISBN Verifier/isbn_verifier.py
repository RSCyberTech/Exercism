def is_valid(isbn):

    numbers = [s if s in "0123456789xX" else -1 for s in isbn if s != "-"]
    if len(numbers) != 10 or -1 in numbers:
        return False

    for n in range(len(numbers) - 1, -1, -1):
        if numbers[n] in "0123456789xX":
            if n + 1 != 10 and numbers[n] in "xX":
                return False
            elif numbers[n] in "xX":
                numbers[n] = 10
            else:
                numbers[n] = int(numbers[n]) * (len(numbers) - n)
        else:
            return False
    return sum(numbers) % 11 == 0
