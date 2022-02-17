import random

print("Welcome to the Guessing Game")

playing = input("Do you want to play the game? ")

if playing.lower() != "yes":
    print("Oh! Thanks for joining in")
    quit()

print("Okay good! Let's play :)")

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range == 0:
        print("Please enter a number greater than 0 next time")
        quit()

else:
    print("Please enter a number next time")
    quit()

random_number = random.randint(0, top_of_range)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Guess a number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please guess a number")
        continue
    
    if user_guess > top_of_range:
        print("Please enter a number between 0 and",top_of_range)
        continue

    if user_guess == random_number:
        print("Congratulations! Your guess is correct.")
        break

    elif user_guess > random_number:
        print("Your guess is greater than the desired number")

    else:
        print("Your guess is smaller than the desired number")

if guess_count == 1:
    print("You guessed it right in",guess_count,"guess.")
else:
    print("You guessed it right in",guess_count,"guesses.")