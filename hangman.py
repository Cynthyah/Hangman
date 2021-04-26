# Game - Hangman
# It has a list of words and you need to try to guess. You have 6 chances.

hangman_steps = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  
You saved me!     
   \O/  
    |   
   / \  
 =========''','''
 
   I died !
     |
   --+--
     |
     |   
 =========''']

def start_game():
    import random
    # list of words to guess
    words = ['fearlessness','brood','galvaniser','draughtiest','cultellus','shying','strassburg','veneer','lanuginous','unlogistical',
             'crookneck','shabbier','install','portsmouth','bucks','websterian','assimilative','heeling','superi','kaltemail']
    # selected a random word from the list
    word = words[random.randint(0,len(words)-1)]
    print("_ "*len(word))
    return word

def choose_letter(word):
    letters = []
    word_choosen = ['_'] * len(word)
    time = 0

    while time < 6:
        is_letter = False
        # show the attempts and ask for a letter
        letter = input(f'\nAttempt {time} -> Choose a letter: ').lower()
        if letter in letters:
            print('\nAlready choosen!')
            continue
        else:
            letters.append(letter)

        for j,l in enumerate(list(word)):
            if l == letter:
                word_choosen[j] = l
                is_letter = True
        if not is_letter:
            time += 1

        # show the picture of hangman(step by step)
        print(hangman_steps[time])
        print("".join(word_choosen),end='')

        # check the word
        if "".join(word_choosen) == word:
            print(hangman_steps[7])
            break

    if time > 5:
       print(hangman_steps[8])
       print(f'\nThe secret word was: {word}')

if __name__ == '__main__':
    print(hangman_steps[0])
    word = start_game()
    choose_letter(word)
