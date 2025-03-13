def sum_of_multiples(limit, multiples):
    output = []
    for r in range(1, limit):
        for m in multiples:
            if m > 0 and (r % m == 0) and r not in output:
                output.append(r)
    return sum(output)
