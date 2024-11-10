def guessing_game():
    print("Welcome to the Number Guessing Game!")

    # Get the range from the user
    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))

        if lower_bound >= upper_bound:
            print("Invalid range. The lower bound must be less than the upper bound.")
            return

        # Generate a random number within the specified range
        number_to_guess = random.randint(lower_bound, upper_bound)
        attempts = 0

        print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
        print("Try to guess it!")

        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
                else:
                    print(
                        f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")

    except ValueError:
        print("Please enter valid numbers for the range.")


guessing_game()
