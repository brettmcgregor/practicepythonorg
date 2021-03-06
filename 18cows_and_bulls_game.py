"""
my record is 7 attempts to guess a four digit number!!!

Create a program that will play the “cows and bulls” game with the user.
The game works like this:

Randomly generate a 4-digit number.
Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user
at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game!
  Enter a number:
  >>> 1234
  2 cows, 0 bulls
  >>> 1256
  1 cow, 1 bull
  ...

Until the user guesses the number.

Features to add:
    catch incorrect guess types (too long, not numbers etc)
    

"""

import random

def game():
    attempts = 0
    previous_guesses = []
    secret_num = []
    num_length = 4

    for i in range(num_length):
        secret_num.append(str(random.randint(0,9)))
    secret_num = "".join(secret_num)
    #print(secret_num)
    print("\n\nTry to guess my four-digit number.\nFor each correct digit \
in your guess you get a 'cow'.\nFor each incorrect digit in your guess \
you get a 'bull'.\n")
    while True:
        bulls = 0
        cows = 0
        guess = input("> ")
        previous_guesses.append(guess)
        print(previous_guesses)
        for i in range(len(secret_num)):
            if guess[i] == secret_num[i]:
                cows += 1
            else:
                bulls += 1
        i += 1
        attempts += 1
        if cows == 4:
            print("You guessed the secret number!!! It was {}.\nIt took you {} attempts"\
                  .format(secret_num, attempts))
            replay = input("Would you like to play again? (Y/n)\n> ")
            if replay.upper() == "N":
                print("OK. See you next time.")
                break
            else:
                game()
        else:
            print("{} cows, {} bulls.".format(cows, bulls))   
               
game()
