def to_rna(dna_strand):
    result = ""
    for dna in dna_strand:
        if dna == "G":
            result = result + "C"
        if dna == "C":
            result = result + "G"    
        if dna == "T":
            result = result + "A"
        if dna == "A":
            result = result + "U"
    return result       