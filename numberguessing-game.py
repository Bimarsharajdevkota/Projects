import random

print("Welcome to the game of guess the number.")
print()
print("You are given a chance to guess a number between 0 and 20. Hope you can get it on your first try!")
print()
print("Let's play.")
print()

# Generate a random number between 0 and 20
secret_number = random.randint(0, 20)
tries = 1

while True:
    try:
        guess = int(input("Now starts the guessing game. Guess the number: "))
        if guess < 0 or guess > 20:
            print("You should read the rule properly. Guess a number between 0 and 20.")
        elif guess < secret_number:
            print("Your guess is low. Guess a higher number.")
            tries += 1
        elif guess > secret_number:
            print("Your guess is high. Guess a lower number.")
            tries += 1
        else:
            print("Your guess is correct!")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 20.")

print(f"You guessed the number in {tries} tries.")
