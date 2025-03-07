import random

# Initialize scores
user_score = 0
computer_score = 0

def get_computer_choice():
    """Randomly selects rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    """Gets the user's choice and validates input."""
    user_input = input("Enter rock, paper, or scissors: ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_input = input("Enter rock, paper, or scissors: ").lower()
    return user_input

def determine_winner(user, computer):
    """Determines the winner of the round."""
    global user_score, computer_score
    
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        user_score += 1
        return "You win this round!"
    else:
        computer_score += 1
        return "Computer wins this round!"

def display_score():
    """Displays the current score."""
    print(f"\nScoreboard: You [{user_score}] - Computer [{computer_score}]\n")

def play_game():
    """Runs the Rock, Paper, Scissors game in a loop until the user quits."""
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

        # Display updated scoreboard
        display_score()

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nFinal Scoreboard:")
            display_score()
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
