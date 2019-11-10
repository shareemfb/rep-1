def isWordGuessed(lettersGuessed, secretWord):
    n = 0
    for i in secretWord:
    	if i in lettersGuessed:
    		n += 1
    boolval = n == len(secretWord)
    return boolval