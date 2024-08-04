import random

number = random.randint(1, 10000)

guess = input("Guess the number and win price: ")
guess = int(guess)

if guess == number:
    print(number)

    print('Congratulations, you guessed the number')

else:
    print(number)
    print(f'The gap between you number and guess is {number - guess} ')
    print('Nothing for you')
    