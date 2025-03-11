import random
import argparse

# This class represents the die used in the game
class Die:
    def __init__(self):
        random.seed(0)  # Ensuring consistency in rolls for testing
    
    def roll(self):
        return random.randint(1, 6)  # Roll the die, returns a number between 1 and 6

# This class represents a player in the game
class Player:
    def __init__(self, name):
        self.name = name  # Player's name
        self.score = 0  # Start with zero points
    
    def reset_score(self):
        self.score = 0  # Reset the player's score when a new game starts

# Main game logic for Pig
class PigGame:
    def __init__(self, num_players=2):
        self.die = Die()  # Create a die object
        self.players = [Player(f'Player {i+1}') for i in range(num_players)]  # Create player objects
        self.current_player_index = 0  # Start with the first player
        self.winning_score = 100  # First to 100 wins!

    # Move to the next player's turn
    def switch_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    # Handles a player's turn
    def play_turn(self):
        player = self.players[self.current_player_index]  # Get the current player
        turn_total = 0  # Points accumulated during this turn
        print(f"{player.name}'s turn! Current score: {player.score}")
        
        while True:
            choice = input("Enter 'r' to roll or 'h' to hold: ").strip().lower()
            if choice == 'r':  # Player chooses to roll
                roll = self.die.roll()
                print(f"Rolled: {roll}")
                if roll == 1:
                    print("Oops! Rolled a 1. No points for this turn.")
                    turn_total = 0  # Lose all turn points
                    break
                else:
                    turn_total += roll  # Add to turn total
                    print(f"Turn total: {turn_total}, Total score if held: {player.score + turn_total}")
            elif choice == 'h':  # Player chooses to hold
                player.score += turn_total  # Add turn points to total score
                print(f"{player.name} holds! Total score: {player.score}")
                break
            else:
                print("Invalid choice. Please enter 'r' to roll or 'h' to hold.")
        
        self.switch_turn()  # Move to the next player's turn
    
    # Handles the overall game loop
    def play_game(self):
        print("Welcome to the Pig Game!")
        while all(player.score < self.winning_score for player in self.players):
            self.play_turn()
        
        winner = max(self.players, key=lambda p: p.score)  # Determine winner
        print(f"{winner.name} wins with a score of {winner.score}!")
        
        self.reset_game()  # Reset game for another round
        
    # Resets the game so players can play again without restarting the script
    def reset_game(self):
        for player in self.players:
            player.reset_score()  # Reset each player's score
        self.current_player_index = 0  # Start from player 1 again
        print("Game reset. Ready for a new round!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--numPlayers", type=int, default=2, help="Number of players in the game")
    args = parser.parse_args()
    
    game = PigGame(num_players=args.numPlayers)  # Create game instance
    while True:
        game.play_game()  # Start the game
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':  # Exit loop if player doesn't want to continue
            break
