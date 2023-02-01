import random
import string
from pathlib import Path

cwd = Path(__file__).parent.absolute()
wordlist_path = f'{cwd}/../words.txt'

def load_words() -> list[str]:
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    with open(wordlist_path, 'r') as file:
        line: str = file.readline()
        wordlist: list[str] = line.split()
    print(f'  {len(wordlist)} words loaded.') 
    return wordlist

def choose_word(wordlist: list[str]) -> str:
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word: str, letters_guessed: list[str]) -> bool:
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    is_guessed: bool = True
    for letter in secret_word:
        if letter not in letters_guessed:
            is_guessed = False
    return is_guessed

def getGuessedWord(secret_word: str, letters_guessed: list[str]) -> str:
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    word: str = ''
    for letter in secret_word:
        if letter in letters_guessed:
            word += letter
        else:
            word += '_ '
    return word

def getAvailableLetters(letters_guessed: list[str]) -> str:
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avalable_letters: str = ''
    alphabet = string.ascii_lowercase
    for letter in alphabet:
        if letter not in letters_guessed:
            avalable_letters += letter
    return avalable_letters

def hangman(secret_word: str) -> None:
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    word_len = len(secret_word)
    print(f'Welcome to the game, Hangman!\nI am thinking of a word that is {word_len} letters long.')

    guesses_left: int = 8
    letters_guessed: list[str] = []
    alphabet = string.ascii_lowercase

    while not is_word_guessed(secret_word, letters_guessed) and guesses_left > 0:
        print('-------------')
        print(f'You have {guesses_left} guesses left.')
        print('Available letters:', getAvailableLetters(letters_guessed))

        guessed_letter = input('Please guess a letter: ').lower()
        blanks = getGuessedWord(secret_word, letters_guessed)

        if len(guessed_letter) > 1:
            print('Sorry, you can guess only 1 letter at a time.')
        elif guessed_letter in letters_guessed:
            print('Oops! You\'ve already guessed that letter:', blanks)
        elif (guessed_letter in alphabet) and (guessed_letter not in letters_guessed):
            letters_guessed.append(guessed_letter)
            blanks = getGuessedWord(secret_word, letters_guessed)
            if guessed_letter in secret_word:
                print('Good guess:', blanks)
            else:
                print('Oops! That letter is not in my word:', blanks)
                guesses_left -= 1
        else:
            print('Sorry, I didn\'t understand that. Recheck your input and try again.')

    print('-------------')
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')


secret_word = choose_word(wordlist).lower()
hangman(secret_word)
