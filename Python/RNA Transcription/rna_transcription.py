def to_rna(dna_strand):
    lookup = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U",
    }
    dna_strand = list(dna_strand)
    for d in range(len(dna_strand)):
        dna_strand[d] = lookup[dna_strand[d]]
    return "".join(dna_strand)
