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


#def get_words(text):
    


def game_play():
    
    open_file = open('words.txt')
    text = open_file.read().split()
    word_bank = [ ]
    for word in text:
        if word != '':
            word_bank.append(word)  
    print(word_bank)              
    return word_bank
    
    


if __name__ == "__main__":
     game_play()
