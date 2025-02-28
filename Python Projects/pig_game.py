# Game rules:
# If a player rolls a 1 their turn is done and their score goes to zero
import random

def roll():
    min_value = 1       # Minimum number when rolling the dice.
    max_value = 6       # Maximum number when rolling the dice.
    roll = random.randint(min_value, max_value)     # Random number between the minimum value and the maximum value.
    return roll

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4.")
    else:
        print("Invalid input, try again.")

max_score = 50      # For the max score in the game.
player_score = [0 for _ in range(players)]      # All players' scores will be stored here and will adjust automatically based on the number of players.


while max(player_score) < max_score: 

    for player_index in range(players):
        print(f"\nPlayer {player_index+1} turn has just started!\n")
        print(f"Your total score is {player_score[player_index]}")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("You rolled a : 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a : {value} !")

            print(f"Your current score is: {current_score}")

        player_score[player_index] += current_score
        print(f"Your total score is: {player_score[player_index]}")

max_score = max(player_score)
winning_index = player_score.index(max_score)

print(f"The winning player is player {winning_index+1} with a score of {max_score}")