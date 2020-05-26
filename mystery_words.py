#guesses - 
    #are invalid if they are two characters, have already been guessed, 
    #need to be compared to the word choosen by the computer
    #should be vaild if upper or lower case

#level-
   #sort words by length
   #easy mode 4-6, normal 6-8, hard 8+

#game-
   #randomly choose word from chosen level
   #print how many characters are in the word, display underscores for each character
   #print guessed characters with _ for characters not guessed yet
   #print letters that have been guessed and turn remaining
   #print message 
   #only remove guesses if guess is incorrect
   # ask start a new round if user wins or loses 

import random



def create_word_bank(opened_text):
    all_words = []
    for word in opened_text:
        if word != '' and word.islower():
            all_words.append(word)
    return all_words     

def determine_level(list_all_words):
    words_to_guess = []
    user_choice = input('What level of difficulty would you like to play at today? Easy, Normal or Hard? ')
    
    if user_choice == 'easy' or 'Easy':
        for word in list_all_words:
         if len(word) >= 4 and len(word) <= 6: 
           words_to_guess.append(word)
           
    
    if user_choice == 'normal' or 'Normal':
       for word in list_all_words:
         if len(word) >= 6 and len(word) <= 8: 
           words_to_guess.append(word) 
    

    if user_choice == 'hard' or 'Hard':
        for word in list_all_words:
         if len(word) >= 8: 
           words_to_guess.append(word) 
    
    return words_to_guess

def random_choice(list_level_words):
    return(random.choices(list_level_words, k = 1))
    

def user_guesses():
    user_input = input(' Please guess one letter: ')
    lower_letter = user_input.lower()
    return lower_letter

def list_of_guesses(letter):
    guesses = [ ]
    guesses.append(letter)
    return guesses

def display_letter(letter, guesses):
    if letter in guesses:
        return letter
    else:
        return '_'

def display_word(word, guesses):
    
    letters_guessed = [display_letter(letter,guesses)for letter in word]
    print(" ".join(letters_guessed))

def game_play():
    
    open_file = open('words.txt')
    text = open_file.read().split()
    total_word_bank = create_word_bank(text)
    level_word_bank = determine_level(total_word_bank)
    random_word = random_choice(level_word_bank)
    number_of_guesses = 8
    
    
    
    
    while True:
        if number_of_guesses > 0:
             print(f'You have {number_of_guesses} guesses left!')
             letters = user_guesses()
             players_guesses = list_of_guesses(letters)
             display = display_word(random_word, players_guesses)
             if letters in random_word:
                 print('You guessed correctly!')
                 print(display)
             elif letters not in random_word:
                 print('You guessed wrong :(')
                 print(display)
                 number_of_guesses -= 1    
        
        elif number_of_guesses <= 0:
            print ('You lost :(')
            return
        
             
             



    
    
        
        
    

                    
    #return word_bank
    
    


if __name__ == "__main__":
     game_play()
