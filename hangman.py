import random
import string
from pathlib import Path

# TODO: rename functions and vars

cwd = Path(__file__).parent.absolute()
WORDLIST_PATH = f'{cwd}/words.txt'

def loadWords() -> list[str]:
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    with open(WORDLIST_PATH, 'r') as file:
        line: str = file.readline()
        wordlist: list[str] = line.split()
    print(f'  {len(wordlist)} words loaded.') 
    return wordlist

def chooseWord(wordlist: list[str]) -> str:
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord: str, lettersGuessed: list[str]) -> bool:
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    isGuessed: bool = True
    for letter in secretWord:
        if letter not in lettersGuessed:
            isGuessed = False
    return isGuessed

def getGuessedWord(secretWord: str, lettersGuessed: list[str]) -> str:
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word: str = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_ '
    return word

def getAvailableLetters(lettersGuessed: list[str]) -> str:
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avalable_letters: str = ''
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in lettersGuessed:
            avalable_letters += letter
    return avalable_letters

def hangman(secretWord: str) -> None:
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    word_len = len(secretWord)
    print(f'Welcome to the game, Hangman!\nI am thinking of a word that is {word_len} letters long.')

    guesses_left: int = 8
    lettersGuessed: list[str] = []
    alphabet = string.ascii_lowercase

    while not isWordGuessed(secretWord, lettersGuessed) and guesses_left > 0:
        print('-------------')
        print(f'You have {guesses_left} guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))

        guessed_letter = input('Please guess a letter: ').lower()
        blanks = getGuessedWord(secretWord, lettersGuessed)

        if len(guessed_letter) > 1:
            print('Sorry, you can guess only 1 letter at a time.')
        elif guessed_letter in lettersGuessed:
            print('Oops! You\'ve already guessed that letter:', blanks)
        elif (guessed_letter in alphabet) and (guessed_letter not in lettersGuessed):
            lettersGuessed.append(guessed_letter)
            blanks = getGuessedWord(secretWord, lettersGuessed)
            if guessed_letter in secretWord:
                print('Good guess:', blanks)
            else:
                print('Oops! That letter is not in my word:', blanks)
                guesses_left -= 1
        else:
            print('Sorry, I didn\'t understand that. Recheck your input and try again.')

    print('-------------')
    if isWordGuessed(secretWord, lettersGuessed):
        print('Congratulations, you won!')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secretWord}.')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
