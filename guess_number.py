number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of or Enter q to quit? ")

    if guess.lower() == 'q':
        print(f'Sorry! The number was {number}')

    guess = int(guess)

    if guess == number:
        print(f'Congrats! You entered the right number')
        break
    else:
        print(f'Sorry! Thats not the correct number. Retry!')
