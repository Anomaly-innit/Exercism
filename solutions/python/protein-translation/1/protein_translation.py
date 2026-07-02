def proteins(strand):
    lists = []
    RNA = {
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
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }
    for i in range(0, len(strand), 3):
        lists.append(strand[i:i + 3])
    result = []
    for row in lists:
        if RNA[row] == "STOP":
            return result
        else:
            result.append(RNA[row])
            
        
    return result
     