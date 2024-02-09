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
    elif guess < number:
        print("Sorry! The number I'm thinking of is higher. Try again.")
    else:
        print("Sorry! The number I'm thinking of is lower. Try again.")
