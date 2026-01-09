def vowel_indices(word):
    vowels = 'aeiouyAEIOUY'
    result = []
    index = 1  

    for char in word:
        if char in vowels:
            result.append(index)
        index += 1

    return result