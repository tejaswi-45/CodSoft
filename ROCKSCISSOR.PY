import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        print("Welcome to Rock, Paper, Scissors Game!")
        print("Choose one of the following: ")
        for i, choice in enumerate(choices):
            print(f"{i+1}. {choice.capitalize()}")
        user_choice_index = int(input("Enter your choice (1/2/3): ")) - 1

        if user_choice_index not in range(3):
            print("Invalid choice! Please try again.")
            continue

        user_choice = choices[user_choice_index]
        computer_choice = random.choice(choices)

        print(f"\nYour choice: {user_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        print(determine_winner(user_choice, computer_choice))

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
