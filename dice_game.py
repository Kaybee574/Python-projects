import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid input, try again.")

max_score = 50
player_scores = [0] * players

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started!")
        print(f"Your total score is: {player_scores[player_idx]}\n")
        current_score = 0

        should_roll = input("Would you like to roll (y)? ")
        if should_roll.lower() != "y":
            break

        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
            print(f"You rolled a: {value}")

        print(f"Your score is: {current_score}")

        player_scores[player_idx] += current_score

print(f"Player {player_scores.index(max(player_scores)) + 1} wins with a score of {max(player_scores)}!")
