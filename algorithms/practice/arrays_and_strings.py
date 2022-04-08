def is_unique(characters):
    """
    Implementation of an algorithm to determinate if a string has all unique characters
    :return: boolean
    """
    english_alphabet = [None] * (ord('z') - ord('a') + 1)
    for character in characters:
        indx = ord(character) - 97
        if english_alphabet[indx] == None:
            english_alphabet[indx] = 1
        else:
            return False

    return True