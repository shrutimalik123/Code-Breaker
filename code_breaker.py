import random

def code_breaker():
    # 1. Setup: Generate a secret 3-digit code as a list of strings
    # We use strings so it's easier to compare with user input later
    secret_code = [str(random.randint(0, 9)) for _ in range(3)]
    attempts = 0
    max_attempts = 10

    print("--- 🔐 Secret Code Breaker 🔐 ---")
    print("I've chosen a 3-digit code (0-9). Can you break it?")
    print(f"You have {max_attempts} attempts.")

    # 2. Game Loop
    while attempts < max_attempts:
        guess = input(f"\nAttempt {attempts + 1}: Enter 3 digits: ").strip()

        # Validation: Ensure the guess is exactly 3 digits
        if len(guess) != 3 or not guess.isdigit():
            print("❌ Invalid! Please enter exactly 3 numbers.")
            continue

        attempts += 1
        
        # 3. Checking Logic
        # Convert guess string into a list of characters
        guess_list = list(guess)
        correct_position = 0

        # Check for numbers that are in the EXACT right spot
        for i in range(3):
            if guess_list[i] == secret_code[i]:
                correct_position += 1

        # 4. Results
        if correct_position == 3:
            print(f"🎉 **JACKPOT!** You broke the code {guess} in {attempts} tries!")
            break
        else:
            print(f"Result: {correct_position} digits are in the correct place.")
            
        if attempts == max_attempts:
            print(f"\n💀 Out of attempts! The code was {''.join(secret_code)}.")

# Start the game
code_breaker()
