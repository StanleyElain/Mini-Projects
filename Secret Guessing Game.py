# A secret word guessing game using functions and loops

secret_word = "passion"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses. Try again!!!")
else:
    print("You win the laptop")