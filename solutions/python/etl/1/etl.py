def transform(legacy_data):

    result = {}
    
    for score, letters in legacy_data.items():
        for letter in letters:
            result.update({letter.lower(): score})
    return result