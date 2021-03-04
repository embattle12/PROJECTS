import random #provides the ability to choose a random word
HANGMAN_PICS = ['''
    +---+                       #HANGMAN_PICS variable's name is in all uppercase. this theis programing convention for the constant variables. 
        |                       #HANGMAN_PICS contains several multiline strings. it can do this because its a list. 
        |                       #bucaus the indexes begin with 0 and not 1 we say that python lists are zero indexed.
        |                       # you can add several lists using the + operator it is known as concatenation
       ===''', '''              #the in operator tells you weather a value is in list or not
    +---+                       
    O   |
        |
        |
       ===''', '''
     +---+
    O   |
    |   |
        |
       ===''', '''
        +---+
    O   |
   /|   |
        |
       ===''', '''
       +---+
    O   |
   /|\  |
        |
       ===''', '''
       +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    O   |
   /|\  |
   / \  |
       ===''']
words = 'Eurytus preprimitive noncharacterized palsgravine bubblingly clericalism speciation santonica overspent completely reconverging Olga perturbedly bangladesh capitalizer diatomic nostalgic xeromorphic blizzard stoic reanchor prototherian Supergenerosity day version sparks spottable reprocess specialise antlered decennary ranunculaceous unavid Inglorious cretan untenantable theca overspecialization toman unidiomatically fonteyn unweariedness macrobiotic preinfect Bumpy liquer helioscopy phocylides leith mains institutionalise putter legal caunus volley Afield phrenologically undiscontinued enterotoxemia hypertherm sollar pronative overenthusiastic valera familiarising impactful Polecat outdeiled overarm effrontery banefully vertebrate dapperness baas unhesitant machabees constraint Unfilterable argonaut paradigmatic mottlement turnstone hostaged pungy haggardly jinsen cuesta transatlantic Gandhara turkistan matte remerge glomma featherback hemorrhage investigate inactively garbanzo mettie Idoism unsensualised undiatonic taming leptorrhiny res boulder monopode epigoneion abbotcy scarp nern araeosystyle morgen unroweled coast sisal state libau pertly banneret photocompose Hypophyllous adrenocorticotrophic unsere jaw cheboygan hahnemann walruses horological gynodioecious plenitude monadically Waveform reduplication hieroglyphology superacquisition unexcrescent deventer ascribe hohenzollern formesoappendix tremble balladier Haunchless siddons reproclamation fleshless bighorn hyperexcursive sicilian venustiano enrapturing firewarden hermes Hamelin italianately acanthite ineptitude zemindari nonacceding monogenist resight fermat alexine venialness'.split()

def getRandomWord(wordList):
    #this function return a random string from the passed list of strings
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    
    print('Missed letters: ', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()
    blanks = '_'*len(secretWord)
    
    for i in range(len(secretWord)): #Replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:# Show the secret word with spaces in between each letter
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    #Returns the letter the player entered. this function makes sure the player entered the single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guss = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter')
        elif guess in alreadyGuessed:
            print('You have already guessed the letter, choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a single LETTER.')
        else:
            return guess
def playAgain():
    #This function returns True if the player wants to play again; otherwise it returns False.
    print('Do yoy want to play again? (Yes or No)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters=''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone=False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)
    #Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters=False
                break
        if foundAllLetters:
            print('Yes! the secret word is "'+ secretWord + '"! You have won')

            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        #check if player has guessed too many times an lost.
        if len(missedLetters) == len(HANGMAN_PICS) -1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\n After ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was " ' + secretWord + '"')
            gameIsDone = True
    # Ask the player if they want to play again, (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters=''
            correctLetters=''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break