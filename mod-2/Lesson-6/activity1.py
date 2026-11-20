# ================================
# NUMBER GUESSING GAME
# ================================

# ---------- SETTINGS (given to you) ----------
secret = 27
max_attempts = 5
count = 0
guess = 0

print("=" * 42)
print(" 🎮 NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ---------- PART 1: the loop and the guess ----------
# YOUR CODE HERE
# Write a while loop that runs while count is less than max_attempts
# AND guess is not equal to secret.
# Inside the loop (indented):
#   read the guess with int(input("Your guess: "))
#   add 1 to count
while guess != secret and count < max_attempts:
    guess = int(input("Your guess: "))
    count += 1
    # ---------- PART 2: win or not ----------
    # YOUR CODE HERE
    # If guess equals secret, print a win message.
    # Otherwise (else), do Parts 3 and 4.
    if guess == secret:
        print("You guessed it!")
    else:
        # ---------- PART 3: distance and hint ----------
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print("🧊 Ice cold!")
        elif diff >= 10:
            print("❄️  Cold!")
        elif diff >= 5:
            print("🌡️  Warm!")
        else:
            print("🔥 Hot!")

        # ---------- PART 4: lives left ----------
        remaining = max_attempts - count
        if remaining > 0:
            print("Lives left: ", end="")
            for i in range(remaining):
                print("❤️ ", end="")
            print()

# ---------- GAME OVER (after the loop) ----------
if guess != secret:
    print("💀 Game over! The secret number was", secret)
