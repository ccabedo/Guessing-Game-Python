secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# loop until the guess the secret word
while guess != secret_word and not(out_of_guesses):
# checks to see if user has used all guesses
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
	print("Out of Guesses, You Lose!")

else:
	print("You win!")