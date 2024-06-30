#Purpose:A number guessing game
#Date:29/03/2024
#Author:g24m5008

import random

def player_guesses(level, guesses, level_rnge):
    """A function that represents a round where the player guesses the number.The function takes in the current level, the number of guesses left, and the range of possible numbers.It returns the updated number of guesses after the round."""
    rng = random.Random()
    com_guess = rng.randrange(0, level_rnge)
    
    player_guess = None
    while guesses > 0:
        player_guess = int(input("Enter a guess:"))
        if player_guess == com_guess:
            print("Well done, you got it")
            guesses += 4
            if level == 10:
                print("You win!!!")
                return guesses
            else:
                print("Good job!!! You are now on level " + str(level + 1))
            break
        elif player_guess > com_guess:
            print("Guess a lower number")
        else:
            print("Guess a higher number")
        guesses -= 1
        if guesses == 0 :
            print("Game over!!!\n The number was:", com_guess)
            return 0
    return guesses

def computer_guesses(level, guesses, level_rnge):
    """A function that represents a round where the computer guesses the number.The function takes in the current level, the number of guesses left, and the range of possible numbers.It returns the updated number of guesses after the round."""
    low = 0
    high = level_rnge
    print("Think of a number between", low, "and", high)
    com_guess = None
    while guesses > 0:
        com_guess = (low + high) // 2
        print("The computer guesses:", com_guess)
        player_hint = input("Is the number too high (H), too low (L), or correct (C)? ")
        if player_hint.upper() == 'C':
            print("The computer got it!")
            guesses += 4
            if level == 10:
                print("The computer wins!!!")
                return guesses
            else:
                print("Good job computer!!! You are now on level " + str(level + 1))
            break
        elif player_hint.upper() == 'H':
            high = com_guess - 1
            print("The computer will guess a lower number next time.")
        else:
            low = com_guess + 1
            print("The computer will guess a higher number next time.")
        guesses -= 1
        if guesses == 0 :
            print("Game over!!! The number was:", com_guess)
            return 0
    return guesses

def main():
    """A main function that controls the flow of the game."""
    guesses = 5
    for level in range(1,11):
        if guesses == 0:
            break 
        game_type = input("Do you want to guess the number (G) or should the computer guess the number (C)? ")
        if game_type.upper() == 'G':
            guesses = player_guesses(level, guesses, (level + 1) * 10)
        else:
            guesses = computer_guesses(level, guesses, (level + 1) * 10)
        if guesses > 0:
            print("Guesses remaining:", guesses)

# Call the main function to start the game
if __name__ == "__main__":
    main()
