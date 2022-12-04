import random
from time import sleep


def guess():
    i = random.randint(1, 10)
    print('guess the number : ')
    guess_input = int(input(">>> "))
    if guess_input == int(i):
        print(f"you guessed the number right! It was {i}")

    elif guess_input != i:
        print(f"you guessed it wrong! It was {i}")
    try_again()


def try_again():
    print('want to play again?')
    try_again_input = input(">>> ")
    if try_again_input == "yes":
        guess()
    elif try_again_input == "no":
        print("bye!")
        return
    else:
        print('please enter a valid response.')
        try_again()


print("what's your name?")
name_input = input(">>> ")
if len(name_input) < 10:
    print(f'Welcome {name_input}')
    sleep(1)
    guess()