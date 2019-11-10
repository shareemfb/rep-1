def getGuessedWord(secretWord, lettersGuessed):
    GuessedWord = ''
    for i in secretWord:
        if i in lettersGuessed:
            GuessedWord += i
        else:
            GuessedWord += '-'
    return GuessedWord