def to_rna(dna_strand):
    if dna_strand == "":
        return ""
    rna = ""
    for letter in dna_strand:
        match(letter):
            case 'G':
                rna += 'C'
                continue
            case 'C':
                rna += 'G'
                continue
            case 'T':
                rna += 'A'
                continue
            case 'A':
                rna += 'U'
                continue
    return rna

