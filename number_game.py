#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tells if the number user inputs is correct

import constants


def main():
    # this function checks if the number user guessed is correct

    # tnput
    guessing_number = int(input("Enter the guessing number:"))
    print("")

    # process and output
    if guessing_number == constants.CORRECT_NUMBER:
        print("Correct!")


if __name__ == "__main__":
    main()
