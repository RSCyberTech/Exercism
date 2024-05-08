def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    div = []
    for n in range(1, (number // 2) + 1):
        if number % n == 0:
            div.append(n)
    div = sum(div)

    return "perfect" if div == number else "abundant" if number < div else "deficient"
