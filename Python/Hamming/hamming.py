def distance(strand_a, strand_b):
    count = 0
    for r in range(len(strand_a) if len(strand_a) > len(strand_b) else len(strand_b)):
        try:
            if strand_a[r] != strand_b[r]:
                count += 1
        except:
            raise ValueError("Strands must be of equal length.")
    return count
