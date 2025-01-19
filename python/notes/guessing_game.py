secret_number = 9
number_of_guesses = 0
maximum_guesses = 3
while number_of_guesses < maximum_guesses:
    guess = int(input('Guess: '))
    number_of_guesses += 1
    if guess == secret_number:
        print('you won')
        break
else:
    print('you lose')
