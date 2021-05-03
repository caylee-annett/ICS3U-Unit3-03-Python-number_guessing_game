#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program is a game where the user tries to guess a randomly
#   generated number


import random


def main():
    # This function tells the user if their guess is correct

    # Input
    guessed_number = int(input("Guess what the number between 0 and 10 is: "))
    print("")

    # Process & Output
    correct_number = random.randint(0, 10)
    if guessed_number == correct_number:
        print("You guessed it!")
    else:
        print("Incorrect! The number was {}.".format(correct_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
