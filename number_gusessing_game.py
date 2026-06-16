import random


def play_game():
    attempt = 0

    try:
        difficulty = int(input(
            "Please enter the difficulty\n"
            "1. Easy\n"
            "2. Medium\n"
            "3. Hard\n"
        ))

        if difficulty not in (1, 2, 3):
            print("Difficulty must be 1, 2, or 3.")
            return

    except ValueError:
        print("Value must be a whole number.")
        return 

    match difficulty:
        case 1:
            secret_number = random.randint(1, 50)
            max_attempt = 12
        case 2:
            secret_number = random.randint(1, 100)
            max_attempt = 10
        case 3:
            secret_number = random.randint(1, 500)
            max_attempt = 7
        
    while max_attempt > 0:
        try:
            guess = int(input("Please enter the number: "))
            attempt += 1
            max_attempt -= 1

            if guess == secret_number:
                print(f"You guessed it in {attempt} attempts!")
                break
            elif guess < secret_number:
                print(f"Too low! Guess higher. {max_attempt} attempts remaining.")
            else:
                print(f"Too high! Guess lower. {max_attempt} attempts remaining.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    else:
        print(f"You have reached the maximum attempts.")
        print(f"The secret number was {secret_number}.")
        print("Thank you for playing!")


while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
