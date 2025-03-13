def proteins(strand):
    inp = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "STOP": ["UAA", "UAG", "UGA"],
    }

    toRet = []
    while len(strand) >= 3:
        print(strand[0:3])
        if strand[0:3] in inp["STOP"]:
            break
        toRet.append(inp[strand[0:3]])
        strand = strand[3:]

    return toRet
