import random

def number_guessing_game():
    """A fun number guessing game."""
    print("=" * 50)
    print("   Welcome to the Number Guessing Game!")
    print("=" * 50)
    
    # Get difficulty level
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-500)")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            max_number = 50
            break
        elif choice == '2':
            max_number = 100
            break
        elif choice == '3':
            max_number = 500
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
    
    # Pick a random number
    secret_number = random.randint(1, max_number)
    attempts = 0
    guessed = False
    
    print(f"\nI'm thinking of a number between 1 and {max_number}...")
    print("Try to guess it!\n")
    
    # Game loop
    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            
            # Validate input
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}!")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                guessed = True
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
                print(f"The number was {secret_number}.")
            elif guess < secret_number:
                print(f"❌ Too low! Try a higher number.")
            else:
                print(f"❌ Too high! Try a lower number.")
                
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    # Ask to play again
    print("\n" + "=" * 50)
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again in ['yes', 'y']:
        print("\n")
        number_guessing_game()
    else:
        print("\nThanks for playing! Goodbye! 👋")
        print("=" * 50)

if __name__ == "__main__":
    number_guessing_game()
