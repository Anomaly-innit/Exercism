def find_anagrams(word, candidates):
    result = []
    for anagram in candidates:
        if sorted(word.lower()) == sorted(anagram.lower()) and word.lower() != anagram.lower():
            result.append(anagram) 
    return result        