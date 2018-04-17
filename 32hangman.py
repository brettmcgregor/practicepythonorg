"""
In this exercise, we will finish building Hangman. In the game of Hangman, the player only
has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the
logic for guessing the letter and displaying that information to the user. In this exercise,
we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following
features:

    Only let the user guess 6 times, and tell the user how many guesses they have left.
    Keep track of the letters the user guessed. If the user guesses a letter they already
    guessed, don’t penalize them - let them guess again.

Optional additions:

   - When the player wins or loses, let them start a new game.
   - Rather than telling the user "You have 4 incorrect guesses left", display some picture
     art for the Hangman. This is challenging - do the other parts of the exercise first!

Your solution will be a lot cleaner if you make use of functions to help you!
"""





#pick a word
import random

with open("sowpods.txt", "r") as f:
    words = list(f)
print(random.choice(words).strip())



#game 
def check_previous(guess, previous_guesses):
    if guess in previous_guesses:
        print("You have already guessed that letter! Try again.")
    else:
        previous_guesses.append(guess)

def check_letter(guess, word, correct_guesses, found):
    for letter in word:
        if guess == letter:
            found.append(guess)
            if guess not in correct_guesses:
                correct_guesses.append(letter)
    if guess not in word:
        print("Incorrect. Try again.")

def print_word(correct_guesses, word):
    for letter in word:
        if letter in correct_guesses:
            print(letter, end = "")
        else:
            print("_ ", end = "")   
            
word = "evaporate"

print("Welcome to Hangman!")
previous_guesses = []
correct_guesses = []
found = []

while True:
    print_word(correct_guesses, word)
    guess = input("\nGuess a letter>  ")
    
    #keep track of previous letters guessed
    check_previous(guess, previous_guesses)
    
    #check if letter is in word
    check_letter(guess,word, correct_guesses, found)

    #check if whole word found
    if len(found) == len(word):
        if len(previous_guesses)-len(correct_guesses) == 1:
            print("Congrats! You guessed the word. You had {} incorrect guess."
              .format(len(previous_guesses)-len(correct_guesses)))
            break
        else:
            print("Congrats! You guessed the word. You had {} incorrect guesses."
                  .format(len(previous_guesses)-len(correct_guesses)))
            break
    
print("Game over")
