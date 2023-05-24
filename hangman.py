import random

# update word list to use word_list from hangman_words.py
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#import logo from hangman_art and print it at start of game
from hangman_art import logo
print(logo)

#testing code
print(f'Pssst, the solution is {chosen_word}')

#create blanks
display = []
for i in range(word_length):
    display += "_"


#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has
#  guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won


while not end_of_game:
    guess = input("Guess a letter: ").lower() 

    #if user has entered a letter they have already guessed print letter and let them know
    if guess in display:
        print(f"You have already guessed {guess}")

    #check guessed letter
    for position in range(word_length):
        i = chosen_word[position]
        if i == guess:
            display[position] = i

    #check if guess is wrong   
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word
        print(f"You guessed {guess}, thats not in word. You lose a life")
        lives -= 1  
        if lives == 0:
            end_of_game = True
            print("You Lose")  
        # use print values to know whats going on in code

    #join all elements in list and turn it into string
    print(f"{''.join(display)}")

    #check if there are no more "_" left in display. Then all letters have been guessed
    if '_' not in display:
        end_of_game = True
        print("You Win")
    
    #import stages from hangman_art.py 
    from hangman_art import stages
    print(stages[lives])
    
    



