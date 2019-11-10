def getAvailableLetters(lettersGuessed):
    import string
    alphabet = string.ascii_lowercase
    availableLetters = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
    