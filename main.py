import random
from game_data import data

def format_data(account):
    """Formats account data into a readable string."""
    return f"{account['name']}, a {account['description']}, from {account['country']}."

def check_answer(user_guess, a_followers, b_followers):
    """Returns True if the user's guess is correct, False otherwise."""
    return (user_guess == "a" and a_followers > b_followers) or (user_guess == "b" and b_followers > a_followers)

def higher_lower_game():
    """Runs the Higher or Lower game."""
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        account_a = account_b
        account_b = random.choice(data)

        # Ensure account_b is not the same as account_a
        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}.")
        print("VS")
        print(f"Compare B: {format_data(account_b)}.")

        # Get user's guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check if the user is correct
        is_correct = check_answer(guess, account_a["follower_count"], account_b["follower_count"])

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False

# Run the game
higher_lower_game()
