def factors(value):
    factors = []
    while value > 1:
        for n in range(2, value + 1):
            if not (value % n):
                factors.append(n)
                value = int(value // n)
                break
    return factors
