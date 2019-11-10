import random
wordList = ["apple", "banana", "cat", "decibel", "elephant", "fiddle", "grace", "hippopotamus", "iridescent", "jeopardy", "kilt", "language", "maneuver", "novice", "optimism", "presumptuous", "quadruple", "radical", "salinometer", "tabernacle", "ubique", "victory", "widget", "xenolith", "yield", "zarzuela"]
secretWord = str(random.choice(wordList).lower())

def isWordGuessed(lettersGuessed, secretWord):
    n = 0
    for i in secretWord:
    	if i in lettersGuessed:
    		n += 1
    boolval = n == len(secretWord)
    return boolval

def getAvailableLetters(lettersGuessed):
    import string
    alphabet = string.ascii_lowercase
    availableLetters = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            availableLetters += letter
    return availableLetters
    
def getGuessedWord(secretWord, lettersGuessed):
    GuessedWord = ''
    for i in secretWord:
        if i in lettersGuessed:
            GuessedWord += i
        else:
            GuessedWord += '-'
    return GuessedWord

def Hangaroo(secretWord):
    numLetters = str(len(secretWord))
    lettersGuessed = []
    mistakesMade = 6
    
    print("Welcome to Hangaroo!")    
    print("The secret word is", numLetters, "letters long.")
    print("//////////")
    
    while (mistakesMade > 0):
     
        if isWordGuessed(lettersGuessed,secretWord):
            print("Congratulations! You guessed the secret word correctly!")
            break
        else:
            pass
        
        print("You have", mistakesMade, "guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Guess a letter: ")
        guessInLowerCase = str(guess.lower())
        
        if guessInLowerCase not in lettersGuessed:
            if guessInLowerCase in secretWord:
                print("Great job!") 
                lettersGuessed.append(guessInLowerCase)
                print(getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Sorry, that letter is not in the secret word:")
                lettersGuessed.append(guessInLowerCase)
                mistakesMade -= 1
                print(getGuessedWord(secretWord, lettersGuessed))
        else:
            print("You already used that letter. Guess another one!")
            print(getGuessedWord(secretWord, lettersGuessed))
            
    else:
        print("Sorry, you already maxed out your guesses. The secret word was:", str(secretWord))