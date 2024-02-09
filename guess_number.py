number = 10
guesses = 5
count = 0

print("I'm thinking of a number...")

while count < guesses:
    count += 1
    tries_left = guesses - count
    guess = input(f"What number am I thinking of or Enter q to quit?  You have {tries_left + 1} attempts left.\n")

    if guess.lower() == 'q':
        print(f'Sorry! The number was {number}')
        break

    guess = int(guess)

    if guess == number:
        print(f'Congrats! You entered the right number')
        break
    else:
        print(f'Sorry! Thats not the correct number. Retry!')

if count == guesses:
    print(f'You have used up all your attempts.')
